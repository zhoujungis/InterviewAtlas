"""命令行入口：采集 -> 归一化 -> 合并 -> 渲染 README。"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

import yaml

from .http import HttpClient
from .normalize import is_foreign_company, normalize_record, refresh_record
from .render import render_site
from .sources import SOURCES
from .storage import load_records, merge_records, record_key, save_records
from .utils import now_cst, today_cst

log = logging.getLogger("main")

DEFAULT_ORDER = ["nowcoder", "mianshiya", "prachub", "juejin"]


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="InterviewAtlas：采集面试经验并生成面经地图")
    parser.add_argument("--config", default="config.yaml", help="配置文件路径")
    parser.add_argument(
        "--source",
        action="append",
        choices=sorted(SOURCES),
        help="只运行指定数据源，可重复传入",
    )
    parser.add_argument("--dry-run", action="store_true", help="只采集和统计，不写文件")
    parser.add_argument(
        "--full",
        action="store_true",
        help="深度采集：使用 full_max_pages / full_company_queries（适合首次或每周全量）",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    config_path = Path(args.config).resolve()
    if not config_path.exists():
        log.error("配置文件不存在：%s", config_path)
        return 2
    config = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    base_dir = config_path.parent

    output_cfg = config.get("output") or {}
    readme_path = base_dir / output_cfg.get("readme", "README.md")
    data_path = base_dir / output_cfg.get("data", "data/interviews")
    interviews_dir = base_dir / output_cfg.get("interviews", "interviews")
    retention_days = int(output_cfg.get("retention_days", 365))

    exclude_sources = set(config.get("exclude_sources") or [])
    exclude_companies = set(config.get("exclude_companies") or [])
    exclude_foreign = bool(config.get("exclude_foreign_companies", True))

    def is_allowed(record: dict) -> bool:
        if record.get("source") in exclude_sources:
            return False
        company = record.get("company") or ""
        if company in exclude_companies:
            return False
        if exclude_foreign and is_foreign_company(company):
            return False
        return True

    client = HttpClient(config.get("crawl") or {})
    raw_items: list[dict] = []
    succeeded = 0
    failed = 0

    existing_raw = load_records(data_path)
    # 旧版单文件数据自动迁移为按公司分片
    migrated_from: Path | None = None
    if not data_path.suffix:
        legacy_path = data_path.parent / f"{data_path.name}.json"
        if not existing_raw and legacy_path.exists():
            log.info("检测到旧版单文件数据 %s，将迁移为按公司分片", legacy_path)
            existing_raw = load_records(legacy_path)
            migrated_from = legacy_path
    known_urls = {record_key(record) for record in existing_raw if record_key(record)}
    known_content = {
        record_key(record)
        for record in existing_raw
        if record_key(record) and len(record.get("content") or "") >= 300
    }

    source_cfg = config.get("sources") or {}
    selected = args.source or [key for key in DEFAULT_ORDER if key in SOURCES]
    companies = config.get("companies") or []
    for key in selected:
        cfg = dict(source_cfg.get(key) or {})
        if not cfg.get("enabled", True):
            log.info("数据源 %s 未启用，跳过", key)
            continue
        cfg["_companies"] = companies
        cfg["_full"] = args.full
        cfg["_known_urls"] = known_urls
        cfg["_known_content"] = known_content
        if args.full and cfg.get("full_max_pages"):
            cfg["max_pages"] = cfg["full_max_pages"]
        source_cls = SOURCES[key]
        source = source_cls(cfg, client)
        log.info(
            "开始采集 %s（%s模式，max_pages=%s）",
            key,
            "全量" if args.full else "增量",
            cfg.get("max_pages"),
        )
        try:
            items = source.fetch()
        except Exception:  # noqa: BLE001
            failed += 1
            log.exception("数据源 %s 采集失败", key)
            continue
        succeeded += 1
        log.info("数据源 %s 采集完成：%s 条原始记录", key, len(items))
        raw_items.extend(items)

    if succeeded == 0:
        log.error("所有数据源均失败，保留现有数据不更新")
        return 1

    normalized: list[dict] = []
    for item in raw_items:
        try:
            record = normalize_record(item)
        except Exception:  # noqa: BLE001
            log.exception("归一化失败：%s", item.get("url"))
            continue
        if record:
            normalized.append(record)

    log.info("原始记录 %s 条，识别为面经 %s 条", len(raw_items), len(normalized))
    normalized = [record for record in normalized if is_allowed(record)]

    today = today_cst()
    updated_at = now_cst()

    # 历史数据用最新规则重算公司与岗位，并剔除国外公司 / 已停用来源
    existing: list[dict] = []
    dropped = 0
    for record in existing_raw:
        refreshed = refresh_record(record)
        if refreshed and is_allowed(refreshed):
            existing.append(refreshed)
        else:
            dropped += 1
    if dropped:
        log.info("历史数据清洗：剔除 %s 条（国外公司或停用来源）", dropped)

    merged, new_count, new_records = merge_records(existing, normalized, today, retention_days)

    log.info(
        "历史 %s 条，合并后 %s 条，本次新增 %s 条",
        len(existing),
        len(merged),
        new_count,
    )

    if args.dry_run:
        log.info("dry-run：跳过写入 %s、%s 和 %s", readme_path, interviews_dir, data_path)
    else:
        save_records(data_path, merged, updated_at)
        render_site(
            merged,
            readme_path=readme_path,
            output_dir=interviews_dir,
            updated_at=updated_at,
            data_rel_path=output_cfg.get("data", "data/interviews"),
            new_count=new_count,
            new_records=new_records,
        )
        if migrated_from:
            migrated_from.unlink(missing_ok=True)
            log.info("旧版单文件数据已迁移并删除：%s", migrated_from)
        log.info("已写入 %s、%s 与 %s", readme_path, interviews_dir, data_path)

    if failed:
        log.warning("有 %s 个数据源失败，本次结果可能不完整", failed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
