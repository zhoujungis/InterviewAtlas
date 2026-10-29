"""数据持久化、去重与合并。

数据按公司分片存放在目录中（`<公司>.json`），避免单个 JSON 逼近 GitHub 的
100MB 文件上限；`load_records` 同时兼容旧的单文件格式。
"""

from __future__ import annotations

import gzip
import json
import logging
import os
from datetime import date, timedelta
from pathlib import Path

from .utils import digest, slugify

log = logging.getLogger(__name__)

META_NAME = "_meta.json"


def record_key(record: dict) -> str:
    url = (record.get("url") or "").split("#")[0].split("?")[0].rstrip("/").lower()
    if url:
        return url
    source = record.get("source") or ""
    external_id = record.get("external_id") or ""
    return f"{source}:{external_id}" if (source or external_id) else (record.get("id") or "")


def load_records(path: Path) -> list[dict]:
    if path.is_dir():
        return _load_shards(path)
    if not path.exists():
        return []
    return _load_payload(path)


def _load_payload(path: Path) -> list[dict]:
    try:
        if path.suffix == ".gz":
            raw = gzip.decompress(path.read_bytes()).decode("utf-8")
        else:
            raw = path.read_text(encoding="utf-8")
        payload = json.loads(raw)
    except (OSError, json.JSONDecodeError, gzip.BadGzipFile) as exc:
        log.warning("读取历史数据失败 %s: %s", path, exc)
        return []
    if isinstance(payload, dict):
        records = payload.get("records") or []
    else:
        records = payload
    return [record for record in records if isinstance(record, dict)]


def _load_shards(directory: Path) -> list[dict]:
    # 同一公司可能同时存在旧 .json 与迁移后的 .json.gz，优先读取压缩版
    files: dict[str, Path] = {}
    for path in directory.iterdir():
        if path.name == META_NAME or not path.name.endswith((".json", ".json.gz")):
            continue
        if path.suffix == ".gz":
            if path.name.endswith(".json.gz"):
                stem = path.name[: -len(".json.gz")] + ".json"
            else:
                stem = path.name[: -len(".gz")]
            files[stem] = path
        else:
            files.setdefault(path.name, path)
    records: list[dict] = []
    for stem in sorted(files):
        records.extend(_load_payload(files[stem]))
    return records


def merge_records(
    existing: list[dict],
    incoming: list[dict],
    today: str,
    retention_days: int,
) -> tuple[list[dict], int, list[dict]]:
    """按 URL 去重合并，返回（合并后的记录, 本次新增条数, 新增记录列表）。"""
    index: dict[str, dict] = {}
    for record in existing:
        key = record_key(record)
        if key:
            index[key] = record

    new_count = 0
    new_records: list[dict] = []
    for record in incoming:
        key = record_key(record)
        if not key:
            continue

        old = index.get(key)
        if old is None:
            record["id"] = record.get("id") or digest(key)
            record["first_seen"] = today
            record["last_seen"] = today
            index[key] = record
            new_count += 1
            new_records.append(record)
            continue

        # 每天都刷 last_seen 会让所有分片日日重写；按月刷新即可满足保留期判断
        if _stale_enough(old.get("last_seen"), today):
            old["last_seen"] = today
        old["title"] = record.get("title") or old.get("title", "")
        old["url"] = record.get("url") or old.get("url", "")
        old["source"] = record.get("source") or old.get("source", "")
        old["external_id"] = record.get("external_id") or old.get("external_id", "")

        new_company = record.get("company") or ""
        if new_company and new_company != "其他公司":
            old["company"] = new_company
        elif not old.get("company"):
            old["company"] = "其他公司"

        new_position = record.get("position") or ""
        if new_position and new_position != "其他岗位":
            old["position"] = new_position
        elif not old.get("position"):
            old["position"] = "其他岗位"

        new_content = record.get("content") or ""
        if len(new_content) > len(old.get("content") or ""):
            old["content"] = new_content
        if record.get("kind") and not old.get("kind"):
            old["kind"] = record["kind"]
        if record.get("published_at") and not old.get("published_at"):
            old["published_at"] = record["published_at"]

    merged = _prune(list(index.values()), today, retention_days)
    merged.sort(key=lambda r: (r.get("company", ""), r.get("position", ""), r.get("published_at") or ""), reverse=True)
    return merged, new_count, new_records


def _stale_enough(last_seen: str | None, today: str) -> bool:
    if not last_seen:
        return True
    try:
        return (date.fromisoformat(today) - date.fromisoformat(last_seen[:10])).days >= 30
    except ValueError:
        return True


def _prune(records: list[dict], today: str, retention_days: int) -> list[dict]:
    if retention_days <= 0:
        return records
    cutoff = date.fromisoformat(today) - timedelta(days=retention_days)
    kept: list[dict] = []
    for record in records:
        last_seen = record.get("last_seen")
        try:
            if last_seen and date.fromisoformat(last_seen[:10]) < cutoff:
                continue
        except ValueError:
            pass
        kept.append(record)
    return kept


def save_records(path: Path, records: list[dict], updated_at: str) -> None:
    if path.suffix == ".json" and not path.is_dir():
        # 兼容仍然配置为单文件路径的旧用法
        _write_json(
            path,
            {"updated_at": updated_at, "total": len(records), "records": records},
        )
        return
    _save_shards(path, records, updated_at)


def _save_shards(directory: Path, records: list[dict], updated_at: str) -> None:
    grouped: dict[str, list[dict]] = {}
    for record in records:
        company = record.get("company") or "其他公司"
        grouped.setdefault(company, []).append(record)

    directory.mkdir(parents=True, exist_ok=True)
    used: dict[str, str] = {}
    written: set[str] = set()
    for company in sorted(grouped):
        name = slugify(company)
        if name in used and used[name] != company:
            name = f"{name}-{digest(company)[:6]}"
        used[name] = company
        filename = f"{name}.json.gz"
        written.add(filename)
        _write_gzip(
            directory / filename,
            {
                "company": company,
                "updated_at": updated_at,
                "count": len(grouped[company]),
                "records": grouped[company],
            },
        )

    # 删除已不存在公司的分片（含迁移前的未压缩分片），避免数据漂移
    for path in list(directory.iterdir()):
        if path.name == META_NAME:
            continue
        if path.name.endswith((".json", ".json.gz")) and path.name not in written:
            path.unlink()

    _write_json(
        directory / META_NAME,
        {
            "updated_at": updated_at,
            "total": len(records),
            "companies": len(grouped),
        },
    )


def _write_json(path: Path, payload: dict) -> None:
    text = json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


def _write_gzip(path: Path, payload: dict) -> None:
    raw = (json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
    # mtime=0 保证相同内容生成完全相同的字节，便于幂等提交
    data = gzip.compress(raw, mtime=0)
    if path.exists() and path.read_bytes() == data:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)
