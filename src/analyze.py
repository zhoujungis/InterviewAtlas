"""调用 GitHub Models 对采集结果做「公司-岗位」与「岗位」两个维度的整合分析。"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import threading
import time
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from datetime import datetime
from pathlib import Path

import requests
import yaml

from .normalize import POSITION_ORDER
from .render import _file_time, _md_escape, _slug, _write_if_changed
from .sources import SOURCE_NAMES
from .storage import load_records
from .utils import CST, now_cst

log = logging.getLogger("analyze")

ENDPOINT = "https://models.github.ai/inference/chat/completions"
# 改动提示词或输出结构时递增，强制所有分析重新生成
PROMPT_VERSION = "2026-10-29.1"

SYSTEM_PROMPT = (
    "你是资深的互联网求职面试研究员，擅长从真实面经中归纳面试流程、考点与题目。"
    "你只依据给定材料作答，材料没有提到的内容必须明确说明样本不足，不得编造。"
)

GROUP_RULES = """请把以下面经整理成一份可直接阅读的分析报告。

要求：
1. 只依据给定材料，不要编造公司流程、薪资、面试轮次或材料中没有出现的题目；材料不足时直接写「样本不足」。
2. 使用二级标题（##），依次输出以下四节：面试流程与轮次、高频考点、典型题目、难度与准备建议。
3. 「典型题目」用无序列表列出 5-10 条，尽量保留原题的表述。
4. 全文 400-800 字，中文，不要输出代码块，不要大段复述原文，不要输出一级标题。
"""

POSITION_RULES = """请把以下各公司的面经分析汇总成一份跨公司对比报告。

要求：
1. 只依据给定材料，不要编造公司名、流程或题目；信息不足时写「样本不足」。
2. 使用二级标题（##），依次输出：岗位整体画像、各公司考察差异、共性高频考点、分阶段准备建议。
3. 「各公司考察差异」用无序列表，每家公司一行，突出与其他公司的差异点。
4. 全文 500-900 字，中文，不要输出代码块，不要输出一级标题。
"""


# ---------------------------------------------------------------------------
# 文本处理
# ---------------------------------------------------------------------------


def _clip(text: str, limit: int) -> str:
    """按段落边界截断，避免把句子切成两半。"""
    value = (text or "").strip()
    if len(value) <= limit:
        return value
    cut = value[:limit]
    idx = max(cut.rfind("\n"), cut.rfind("。"), cut.rfind("！"), cut.rfind("？"))
    if idx > limit * 0.6:
        cut = cut[: idx + 1]
    return cut.rstrip() + "\n（后文略）"


def _clean_markdown(text: str) -> str:
    value = (text or "").strip()
    value = value.replace("\r\n", "\n")
    if value.startswith("```"):
        value = value.split("\n", 1)[-1]
    if value.endswith("```"):
        value = value[: -3].rstrip()
    lines = value.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and lines[0].lstrip().startswith("# "):
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


GROUP_SECTIONS = ("面试流程与轮次", "高频考点", "典型题目", "难度与准备建议")
POSITION_SECTIONS = ("岗位整体画像", "各公司考察差异", "共性高频考点", "分阶段准备建议")


def _dedupe(records: list[dict]) -> list[dict]:
    """同一篇面经被多个关键词 / 来源重复收录时只保留一条。"""
    seen: set[str] = set()
    unique: list[dict] = []
    for record in sorted(records, key=lambda item: len(item.get("content") or ""), reverse=True):
        title = (record.get("title") or "").strip()
        key = f"{title}|{re.sub(r'\\s+', '', (record.get('content') or '')[:120])}"
        if key in seen:
            continue
        seen.add(key)
        unique.append(record)
    return unique


def _pick_records(records: list[dict], max_records: int) -> list[dict]:
    """一半取正文最长的（信息量大），一半取最新的（贴近当下流程）。"""
    pool = _dedupe(records)
    longest = sorted(pool, key=lambda item: len(item.get("content") or ""), reverse=True)
    recent = sorted(pool, key=lambda item: item.get("published_at") or "", reverse=True)
    half = max(max_records // 2, 1)
    picked: list[dict] = []
    for record in longest[:half] + recent[: max_records - half]:
        if record not in picked:
            picked.append(record)
    for record in longest:
        if len(picked) >= max_records:
            break
        if record not in picked:
            picked.append(record)
    return picked[:max_records]


def _samples(
    records: list[dict],
    *,
    max_records: int,
    max_chars_per_record: int,
    max_prompt_chars: int,
) -> tuple[list[dict], str]:
    ranked = _pick_records(records, max_records)
    ranked.sort(key=lambda item: item.get("published_at") or "", reverse=True)

    blocks: list[str] = []
    used = 0
    picked: list[dict] = []
    for index, record in enumerate(ranked, 1):
        body = _clip(record.get("content") or "", max_chars_per_record)
        if len(body) < 80:
            continue
        source = SOURCE_NAMES.get(record.get("source") or "", record.get("source") or "")
        header = (
            f"【面经 {index}】{record.get('title') or '未命名'}"
            f"（{record.get('published_at') or '日期未知'} · {source}）"
        )
        block = f"{header}\n{body}"
        if blocks and used + len(block) > max_prompt_chars:
            break
        blocks.append(block)
        picked.append(record)
        used += len(block)
    return picked, "\n\n".join(blocks)


def _sample_span(records: list[dict]) -> str:
    dates = sorted(record.get("published_at") or "" for record in records)
    dates = [date for date in dates if date]
    if not dates:
        return "时间未知"
    return f"{dates[0]} ~ {dates[-1]}"


def _missing_sections(body: str, sections: tuple[str, ...]) -> list[str]:
    return [section for section in sections if f"## {section}" not in body]


def _group_key(company: str, position: str) -> str:
    return f"{company}||{position}"


def _rel(target: Path, start: Path) -> str:
    return os.path.relpath(target, start).replace(os.sep, "/")


# ---------------------------------------------------------------------------
# 模型调用
# ---------------------------------------------------------------------------


class ModelError(RuntimeError):
    """模型调用失败。"""


class QuotaExceeded(ModelError):
    """额度用尽，应停止本次运行剩余调用。"""


class AuthError(ModelError):
    """权限或凭据错误，重试无意义。"""


class Analyzer:
    """带全局限速与重试的 GitHub Models 客户端。"""

    def __init__(self, config: dict, model: str):
        self.model = model
        self.timeout = float(config.get("timeout", 90))
        self.retries = int(config.get("retries", 3))
        self.interval = 60.0 / max(float(config.get("rpm", 12)), 1.0)
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""
        if not token:
            raise RuntimeError("缺少 GITHUB_TOKEN，无法调用 GitHub Models")
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
                "X-GitHub-Api-Version": "2022-11-28",
            }
        )
        self._lock = threading.Lock()
        self._next_at = 0.0

    def _wait_turn(self) -> None:
        with self._lock:
            now = time.monotonic()
            if now < self._next_at:
                time.sleep(self._next_at - now)
            self._next_at = max(now, self._next_at) + self.interval

    def chat(self, user: str) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user},
            ],
            "temperature": 0.3,
            "max_tokens": 1600,
        }
        last_error = ""
        for attempt in range(1, self.retries + 1):
            self._wait_turn()
            try:
                resp = self.session.post(ENDPOINT, json=payload, timeout=self.timeout)
            except requests.RequestException as exc:
                last_error = f"网络错误：{exc}"
            else:
                if resp.status_code == 200:
                    data = resp.json()
                    content = (data.get("choices") or [{}])[0].get("message", {}).get("content")
                    if content and content.strip():
                        return content
                    last_error = "模型返回为空"
                elif resp.status_code in (401, 403):
                    text = resp.text[:200]
                    if resp.status_code == 403 and "rate limit" in text.lower():
                        raise QuotaExceeded(f"403 限流：{text}")
                    raise AuthError(
                        f"{resp.status_code} 权限错误：{text}"
                        "（请确认 workflow 已设置 permissions: models: read）"
                    )
                elif resp.status_code == 429:
                    text = resp.text[:160]
                    if resp.headers.get("x-ratelimit-remaining") == "0":
                        raise QuotaExceeded(f"429 当日额度已用尽：{text}")
                    retry_after = resp.headers.get("Retry-After")
                    wait_seconds = (
                        min(float(retry_after), 60)
                        if retry_after and retry_after.replace(".", "").isdigit()
                        else 30
                    )
                    last_error = f"429 限流：{text}"
                    log.warning(
                        "触发限流，等待 %.0fs 后重试（%s/%s）", wait_seconds, attempt, self.retries
                    )
                    time.sleep(wait_seconds)
                    continue
                else:
                    last_error = f"{resp.status_code}：{resp.text[:200]}"
                    if resp.status_code < 500:
                        break
            log.warning("模型调用失败（%s/%s）：%s", attempt, self.retries, last_error)
            time.sleep(min(2 ** attempt, 20))
        raise ModelError(last_error)


# ---------------------------------------------------------------------------
# 分析写入
# ---------------------------------------------------------------------------


def _write_group(
    analyzer: Analyzer,
    *,
    company: str,
    position: str,
    records: list[dict],
    analysis_dir: Path,
    interviews_dir: Path,
    options: dict,
) -> str:
    picked, sample = _samples(
        records,
        max_records=int(options.get("max_records_per_group", 8)),
        max_chars_per_record=int(options.get("max_chars_per_record", 1200)),
        max_prompt_chars=int(options.get("max_prompt_chars", 16000)),
    )
    if not sample:
        raise RuntimeError("没有可用正文")
    user = (
        f"公司：{company}\n岗位：{position}\n"
        f"材料共 {len(records)} 条面经，以下为 {len(picked)} 条较完整的样本"
        f"（发布时间 {_sample_span(picked)}）：\n\n{sample}\n\n"
        f"材料中可能混有与「{position}」无关的帖子，只提取与该岗位相关的内容。\n\n"
        f"{GROUP_RULES}"
    )
    body = _clean_markdown(analyzer.chat(user))
    missing = _missing_sections(body, GROUP_SECTIONS)
    if missing:
        retry = _clean_markdown(
            analyzer.chat(
                user
                + "\n\n注意：输出必须严格包含以下四个二级标题："
                "「## 面试流程与轮次」「## 高频考点」「## 典型题目」"
                "「## 难度与准备建议」，缺少任何一节视为不合格，请重新输出完整报告。"
            )
        )
        if len(_missing_sections(retry, GROUP_SECTIONS)) <= len(missing):
            body = retry
            missing = _missing_sections(body, GROUP_SECTIONS)
        if missing:
            body = f"> 注：本次生成缺少「{'、'.join(missing)}」小节。\n\n{body}"

    file_path = analysis_dir / _slug(company) / f"{_slug(position)}.md"
    source = _rel(interviews_dir / _slug(company) / f"{_slug(position)}.md", file_path.parent)
    content = "\n".join(
        [
            f"# {company} · {position} 面经整合分析",
            "",
            f"> 基于 **{len(records):,}** 条面经（分析样本 {len(picked)} 条，"
            f"发布时间 {_sample_span(picked)}）自动生成 ｜ "
            f"模型 `{analyzer.model}` ｜ 更新 {now_cst()}（UTC+8）",
            f"> 原始面经：[{company} / {position}]({source})",
            "",
            body,
            "",
            "---",
            "",
            "> 本页由 GitHub Models 自动生成，可能存在偏差或遗漏，请以[原始面经]"
            f"({source}) 为准。",
            "",
        ]
    )
    _write_if_changed(file_path, content)
    return f"{_slug(company)}/{_slug(position)}.md"


def _write_position(
    analyzer: Analyzer,
    *,
    position: str,
    companies: list[tuple[str, int]],
    analysis_dir: Path,
    readme_path: Path,
    options: dict,
) -> str:
    limit = int(options.get("max_companies_per_position", 16))
    chars = int(options.get("max_chars_per_company", 700))
    parts: list[str] = []
    included: list[tuple[str, int]] = []
    for company, count in sorted(companies, key=lambda item: item[1], reverse=True)[:limit]:
        file_path = analysis_dir / _slug(company) / f"{_slug(position)}.md"
        if not file_path.exists():
            continue
        text = file_path.read_text(encoding="utf-8")
        body = text.split("\n", 1)[1] if text.startswith("# ") else text
        body = body.split("\n---\n")[0].strip()
        body = "\n".join(
            line for line in body.splitlines()
            if not line.startswith("> ") and not line.startswith("# ")
        ).strip()
        if not body:
            continue
        parts.append(f"【{company}】（{count} 条面经）\n{_clip(body, chars)}")
        included.append((company, count))
    if len(included) < int(options.get("position_min_companies", 3)):
        raise RuntimeError(f"可用公司分析不足（{len(included)} 家）")

    user = (
        f"岗位：{position}\n以下为 {len(included)} 家公司的面经分析摘要：\n\n"
        + "\n\n".join(parts)
        + f"\n\n{POSITION_RULES}"
    )
    body = _clean_markdown(analyzer.chat(user))
    missing = _missing_sections(body, POSITION_SECTIONS)
    if missing:
        retry = _clean_markdown(
            analyzer.chat(
                user
                + "\n\n注意：输出必须严格包含以下四个二级标题："
                "「## 岗位整体画像」「## 各公司考察差异」「## 共性高频考点」"
                "「## 分阶段准备建议」，缺少任何一节视为不合格，请重新输出完整报告。"
            )
        )
        if len(_missing_sections(retry, POSITION_SECTIONS)) <= len(missing):
            body = retry
            missing = _missing_sections(body, POSITION_SECTIONS)
        if missing:
            body = f"> 注：本次生成缺少「{'、'.join(missing)}」小节。\n\n{body}"

    file_path = analysis_dir / "by-position" / f"{_slug(position)}.md"
    back = _rel(readme_path, file_path.parent)
    company_rows: list[str] = []
    for company, count in sorted(included, key=lambda item: item[1], reverse=True):
        company_file = analysis_dir / _slug(company) / f"{_slug(position)}.md"
        company_rows.append(
            f"| {_md_escape(company)} | {count:,} | [{company} / {position}]"
            f"({_rel(company_file, file_path.parent)}) |"
        )
    content = "\n".join(
        [
            f"# {position} 岗位跨公司面经分析",
            "",
            f"> 汇总 **{len(included)}** 家公司 ｜ 模型 `{analyzer.model}` ｜ 更新 {now_cst()}（UTC+8）",
            f"> 返回：[分析总目录]({back})",
            "",
            body,
            "",
            "## 纳入分析的公司",
            "",
            "| 公司 | 面经条数 | 分析文件 |",
            "| --- | ---: | --- |",
            *company_rows,
            "",
            "---",
            "",
            "> 本页由 GitHub Models 自动生成，请结合公司维度的原始面经核对。",
            "",
        ]
    )
    _write_if_changed(file_path, content)
    return f"by-position/{_slug(position)}.md"


def _render_index(
    *,
    analysis_dir: Path,
    readme_path: Path,
    manifest: dict,
    total_groups: int,
    eligible_groups: int,
    updated_at: str,
    model: str,
    skipped: list[str] | None = None,
) -> None:
    groups = manifest.get("groups") or {}
    positions = manifest.get("positions") or {}
    remaining = max(0, eligible_groups - len(groups))
    lines = [
        "# InterviewAtlas · 面经整合分析",
        "",
        "> 由 GitHub Models 基于 [原始面经](../interviews) 自动生成，"
        "分为「公司-岗位」与「岗位」两个维度，原始数据见 [data/interviews](../data/interviews)。",
        "",
        "> 返回：[总目录](../README.md)",
        "",
        f"- 最后更新：{updated_at}（UTC+8）",
        f"- 模型：`{model}`",
        f"- 已分析：**{len(groups)}** / {eligible_groups} 个达标公司-岗位组"
        f"（全部 {total_groups} 个组中，条数达标的才会分析）",
    ]
    if remaining:
        lines.append(f"- 待分析：**{remaining}** 个组，将在后续每日运行中按额度逐步补齐")
    if skipped:
        lines.append(f"- 不参与分析：{'、'.join(skipped)}（混合来源，无法做有意义的归纳）")
    lines += [
        "",
        "## 岗位维度",
        "",
        "| 岗位 | 覆盖公司 | 文件 | 最后更新（UTC+8） |",
        "| --- | ---: | --- | --- |",
    ]
    for position in POSITION_ORDER:
        entry = positions.get(position)
        if not entry:
            continue
        path = analysis_dir / entry["file"]
        lines.append(
            f"| {_md_escape(position)} | {entry.get('companies', 0):,} | "
            f"[{entry['file']}]({entry['file']}) | {_file_time(path)} |"
        )
    lines += [
        "",
        "## 公司-岗位维度",
        "",
        "| 公司 | 岗位 | 面经条数 | 文件 | 最后更新（UTC+8） |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for key in sorted(groups, key=lambda item: (groups[item].get("company") != "其他公司",
                                                -groups[item].get("count", 0),
                                                groups[item].get("company", ""),
                                                groups[item].get("position", ""))):
        entry = groups[key]
        path = analysis_dir / entry["file"]
        lines.append(
            f"| {_md_escape(entry.get('company', ''))} | {_md_escape(entry.get('position', ''))} | "
            f"{entry.get('count', 0):,} | [{entry['file']}]({entry['file']}) | {_file_time(path)} |"
        )
    lines += [
        "",
        "---",
        "",
        "> 分析内容由模型生成，可能存在偏差，请以[原始面经](../interviews)为准。",
        "",
    ]
    _write_if_changed(readme_path, "\n".join(lines))


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="InterviewAtlas：用 GitHub Models 生成面经整合分析")
    parser.add_argument("--config", default="config.yaml", help="配置文件路径")
    parser.add_argument("--dry-run", action="store_true", help="只统计待分析组数，不调用模型")
    parser.add_argument("--force", action="store_true", help="忽略缓存，重新生成所有分析")
    parser.add_argument("--limit", type=int, help="本次最多调用多少次模型（覆盖配置）")
    parser.add_argument("--model", help="覆盖配置中的模型名")
    parser.add_argument("--only", help="只分析指定公司或岗位，便于调试")
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
    options = config.get("analysis") or {}
    data_path = base_dir / output_cfg.get("data", "data/interviews")
    interviews_dir = base_dir / output_cfg.get("interviews", "interviews")
    analysis_dir = base_dir / options.get("output", "analysis")
    model = args.model or options.get("model", "openai/gpt-4o-mini")
    max_calls = args.limit if args.limit is not None else int(options.get("max_calls_per_run", 120))
    min_records = int(options.get("min_records", 20))
    refresh_days = int(options.get("refresh_after_days", 30))

    if not data_path.exists():
        log.error("数据文件不存在：%s", data_path)
        return 2
    records: list[dict] = load_records(data_path)

    grouped: dict[tuple[str, str], list[dict]] = {}
    for record in records:
        company = record.get("company") or "其他公司"
        position = record.get("position") or "其他岗位"
        grouped.setdefault((company, position), []).append(record)

    company_exclude = {str(item) for item in (options.get("company_exclude") or [])}
    position_exclude = {str(item) for item in (options.get("position_exclude") or [])}
    skip_keys = {
        key for key in grouped
        if key[0] in company_exclude or key[1] in position_exclude
    }

    eligible = {
        key: value for key, value in grouped.items()
        if len(value) >= min_records and key not in skip_keys
    }
    if args.only:
        eligible = {
            key: value for key, value in eligible.items()
            if args.only in key[0] or args.only in key[1]
        }

    manifest_path = analysis_dir / "manifest.json"
    manifest: dict = {}
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            log.warning("manifest 解析失败，将重建")
    if manifest.get("version") != PROMPT_VERSION or manifest.get("model") != model:
        log.info("无可用缓存（首次运行，或提示词版本 / 模型变化），忽略旧结果")
        manifest = {"version": PROMPT_VERSION, "model": model, "groups": {}, "positions": {}}
    manifest.setdefault("groups", {})
    manifest.setdefault("positions", {})
    # 已排除的兜底分类不保留旧分析记录
    for key, entry in list(manifest["groups"].items()):
        if entry.get("company") in company_exclude or entry.get("position") in position_exclude:
            manifest["groups"].pop(key)
    for position in position_exclude:
        manifest["positions"].pop(position, None)

    def _stale(entry: dict | None, count: int, path: Path) -> bool:
        if args.force or not entry or not path.exists():
            return True
        if count - int(entry.get("count", 0)) >= max(5, int(count * 0.1)):
            return True
        try:
            stamp = datetime.strptime(entry.get("analyzed_at", ""), "%Y-%m-%d %H:%M")
        except ValueError:
            return True
        return (datetime.now(CST).replace(tzinfo=None) - stamp).days >= refresh_days

    pending: list[tuple[str, int, tuple[str, str], list[dict]]] = []
    for key, group_records in eligible.items():
        company, position = key
        entry = manifest["groups"].get(_group_key(company, position))
        path = analysis_dir / _slug(company) / f"{_slug(position)}.md"
        if _stale(entry, len(group_records), path):
            pending.append((company, position, key, group_records))
    # 先分析公司记录多、真实公司优先的组
    pending.sort(key=lambda item: (item[0] == "其他公司", -len(item[3]), item[0], item[1]))

    position_count = len({position for _, position in eligible})
    reserve = min(position_count, max_calls // 6)
    group_budget = max(0, max_calls - reserve)
    selected = pending[:group_budget]

    log.info(
        "达标组 %s 个，待分析 %s 个；本次预算 %s 次（公司-岗位 %s 次 + 岗位 %s 次）",
        len(eligible), len(pending), max_calls, len(selected), reserve,
    )

    if args.dry_run:
        for company, position, _, group_records in selected[:5]:
            picked, sample = _samples(
                group_records,
                max_records=int(options.get("max_records_per_group", 8)),
                max_chars_per_record=int(options.get("max_chars_per_record", 1200)),
                max_prompt_chars=int(options.get("max_prompt_chars", 16000)),
            )
            log.info(
                "示例组 %s / %s：%s 条，样本 %s 条，提示词 %s 字",
                company, position, len(group_records), len(picked), len(sample),
            )
        return 0

    try:
        analyzer = Analyzer(options, model)
    except RuntimeError as exc:
        log.error("%s", exc)
        return 2

    groups = manifest["groups"]
    changed_positions: set[str] = set()
    failed = 0
    done_groups = 0
    fatal: str | None = None
    updated_at = now_cst()

    if selected:
        workers = max(1, int(options.get("workers", 2)))
        job_iter = iter(selected)
        with ThreadPoolExecutor(max_workers=workers) as pool:
            in_flight: dict = {}

            def submit_next() -> bool:
                task = next(job_iter, None)
                if task is None:
                    return False
                company, position, _, group_records = task
                future = pool.submit(
                    _write_group,
                    analyzer,
                    company=company,
                    position=position,
                    records=group_records,
                    analysis_dir=analysis_dir,
                    interviews_dir=interviews_dir,
                    options=options,
                )
                in_flight[future] = (company, position, len(group_records))
                return True

            for _ in range(workers):
                submit_next()
            while in_flight:
                finished, _ = wait(in_flight, return_when=FIRST_COMPLETED)
                for future in finished:
                    company, position, count = in_flight.pop(future)
                    try:
                        rel_path = future.result()
                    except (QuotaExceeded, AuthError) as exc:
                        fatal = str(exc)
                        log.error("停止后续分析：%s", exc)
                        continue
                    except ModelError as exc:
                        failed += 1
                        log.warning("分析失败 %s / %s：%s", company, position, exc)
                        continue
                    groups[_group_key(company, position)] = {
                        "company": company,
                        "position": position,
                        "count": count,
                        "file": rel_path,
                        "analyzed_at": now_cst(),
                    }
                    changed_positions.add(position)
                    done_groups += 1
                    log.info("已生成 %s / %s（%s 条）", company, position, count)
                if fatal:
                    job_iter = iter(())
                while not fatal and len(in_flight) < workers and submit_next():
                    pass

    # 岗位维度：覆盖公司数达标的岗位都生成，纳入的公司分析有变化则刷新
    positions = manifest["positions"]
    position_jobs: list[tuple[str, list[tuple[str, int]]]] = []
    for position in {key[1] for key in eligible}:
        companies = [
            (entry["company"], int(entry.get("count", 0)))
            for entry in groups.values()
            if entry.get("position") == position
        ]
        if len(companies) < int(options.get("position_min_companies", 3)):
            continue
        entry = positions.get(position)
        path = analysis_dir / "by-position" / f"{_slug(position)}.md"
        if position in changed_positions or args.force or not entry or not path.exists():
            position_jobs.append((position, companies))
        elif _stale(entry, len(companies), path):
            position_jobs.append((position, companies))

    position_jobs.sort(key=lambda item: -len(item[1]))
    budget_left = max(0, max_calls - len(selected) - failed)
    log.info("岗位维度待生成 %s 个，本次额度剩余 %s 次", len(position_jobs), budget_left)

    done_positions = 0
    for position, companies in position_jobs[:budget_left]:
        if fatal:
            break
        try:
            rel_path = _write_position(
                analyzer,
                position=position,
                companies=companies,
                analysis_dir=analysis_dir,
                readme_path=analysis_dir / "README.md",
                options=options,
            )
        except (QuotaExceeded, AuthError) as exc:
            fatal = str(exc)
            log.error("停止后续分析：%s", exc)
            break
        except Exception as exc:  # noqa: BLE001
            failed += 1
            log.warning("岗位分析失败 %s：%s", position, exc)
            continue
        positions[position] = {
            "companies": min(len(companies), int(options.get("max_companies_per_position", 16))),
            "file": rel_path,
            "analyzed_at": now_cst(),
            "count": len(companies),
        }
        done_positions += 1
        log.info("已生成岗位分析 %s（%s 家公司）", position, len(companies))

    manifest["updated_at"] = updated_at
    manifest["eligible_groups"] = len(eligible)
    manifest["total_groups"] = len(grouped)
    analysis_dir.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )

    _render_index(
        analysis_dir=analysis_dir,
        readme_path=analysis_dir / "README.md",
        manifest=manifest,
        total_groups=len(grouped),
        eligible_groups=len(eligible),
        updated_at=updated_at,
        model=model,
        skipped=[
            name for name in [*sorted(company_exclude), *sorted(position_exclude)]
            if name
        ],
    )

    remaining = len(pending) - len(selected)
    log.info(
        "完成：公司-岗位新增 %s 个、岗位 %s 个、失败 %s 个；仍有 %s 个组待后续运行",
        done_groups,
        done_positions,
        failed,
        remaining,
    )

    if fatal:
        return 1
    if failed and done_groups + done_positions == 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
