"""按公司/岗位拆分 Markdown 文件，并生成精简的 README 索引。"""

from __future__ import annotations

import os
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from .normalize import POSITION_ORDER
from .sources import SOURCE_NAMES

SOURCE_METHODS = {
    "nowcoder": "站内搜索接口",
    "mianshiya": "企业题库 + 面试题",
    "juejin": "站内搜索接口 + 文章全文",
}


def _md_escape(text: str) -> str:
    return text.replace("[", "\\[").replace("]", "\\]").replace("\n", " ")


def _slug(text: str) -> str:
    value = (text or "未分类").replace("/", "-").replace("\\", "-")
    value = re.sub(r'[<>:"|?*#%\[\]]', "", value).strip(" .")
    return value or "未分类"


def _record_sort_key(record: dict) -> tuple[str, str]:
    return (record.get("published_at") or "", record.get("first_seen") or "")


def _position_sort_key(item: tuple[str, list[dict]]) -> tuple[int, int]:
    position, records = item
    idx = POSITION_ORDER.index(position) if position in POSITION_ORDER else len(POSITION_ORDER)
    return (idx, -len(records))


def _company_sort_key(item: tuple[str, dict[str, list[dict]]]) -> tuple[int, int, str]:
    company, positions = item
    total = sum(len(v) for v in positions.values())
    return (1 if company == "其他公司" else 0, -total, company)


def _file_time(path: Path) -> str:
    if not path.exists():
        return "-"
    return datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M")


def _write_if_changed(path: Path, content: str) -> None:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _render_group_file(
    company: str,
    position: str,
    records: list[dict],
    readme_rel: str,
) -> str:
    lines = [
        f"# {company} · {position}",
        "",
        f"> 共 **{len(records):,}** 条 ｜ [返回总目录]({readme_rel})",
        "",
        "---",
        "",
    ]
    for record in sorted(records, key=_record_sort_key, reverse=True):
        title = _md_escape(record.get("title") or "未命名面经")
        source_name = SOURCE_NAMES.get(record.get("source") or "", record.get("source") or "")
        kind = record.get("kind") or "面经"
        published = record.get("published_at") or record.get("first_seen") or ""
        url = record.get("url") or ""
        lines.append(f"## {title}")
        lines.append("")
        meta = " ｜ ".join(
            part
            for part in [f"来源：{source_name}", f"类型：{kind}", f"发布：{published}" if published else ""]
            if part
        )
        lines.append(f"{meta} ｜ [原文链接]({url})")
        lines.append("")
        content = (record.get("content") or record.get("summary") or "").strip()
        if content:
            lines.append(content)
        else:
            lines.append("> 原站未提供正文，请点击原文链接查看。")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_site(
    records: list[dict],
    *,
    readme_path: Path,
    output_dir: Path,
    updated_at: str,
    data_rel_path: str,
    new_count: int,
    new_records: list[dict],
) -> None:
    """生成 interviews/<公司>/<岗位>.md 与 README 索引。"""
    grouped: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for record in records:
        grouped[record.get("company") or "其他公司"][record.get("position") or "其他岗位"].append(record)

    sorted_companies = sorted(grouped.items(), key=_company_sort_key)

    table_rows: list[str] = []
    expected_files: set[Path] = set()
    group_count = 0
    for company, positions in sorted_companies:
        for position, pos_records in sorted(positions.items(), key=_position_sort_key):
            group_count += 1
            file_path = output_dir / _slug(company) / f"{_slug(position)}.md"
            expected_files.add(file_path)
            readme_rel = os.path.relpath(readme_path, file_path.parent).replace(os.sep, "/")
            content = _render_group_file(company, position, pos_records, readme_rel)
            _write_if_changed(file_path, content)
            rel_path = os.path.relpath(file_path, readme_path.parent).replace(os.sep, "/")
            table_rows.append(
                f"| {_md_escape(company)} | {_md_escape(position)} | {len(pos_records):,} | "
                f"[{rel_path}]({rel_path}) | {_file_time(file_path)} |"
            )

    # 清理已不存在的公司/岗位文件
    if output_dir.exists():
        for old_file in output_dir.rglob("*.md"):
            if old_file not in expected_files:
                old_file.unlink()
        for directory in sorted(output_dir.rglob("*"), reverse=True):
            if directory.is_dir() and not any(directory.iterdir()):
                directory.rmdir()

    total = len(records)
    company_count = len(grouped)
    source_counts = Counter(record.get("source") or "" for record in records)
    position_counts = Counter(record.get("position") or "其他岗位" for record in records)

    lines: list[str] = [
        "# InterviewAtlas · 面经地图",
        "",
        "> 自动采集 **牛客网 / 面试鸭 / 掘金** 的国内公司面试经验，按「公司 / 岗位」拆分成可检索的面经地图。"
        "本页只维护文件路径、修改时间与更新摘要。",
        "",
        f"- 最后更新：{updated_at}（UTC+8）",
        f"- 累计收录：**{total:,}** 条，覆盖 **{company_count}** 家公司、**{group_count}** 个公司-岗位文件",
        f"- 本次运行新增：**{new_count:,}** 条",
        f"- 原始数据：[{data_rel_path}]({data_rel_path})",
        "- 分析报告：[analysis/README.md](analysis/README.md)（公司-岗位 + 岗位维度）",
        "",
    ]

    if total == 0:
        lines.extend(["> 本次未采集到数据，请稍后重试。", ""])

    lines.extend(["## 来源分布", "", "| 来源 | 条数 | 采集方式 |", "| --- | ---: | --- |"])
    for source, count in source_counts.most_common():
        if source:
            lines.append(
                f"| {SOURCE_NAMES.get(source, source)} | {count:,} | {SOURCE_METHODS.get(source, '网页解析')} |"
            )
    lines.append("")

    lines.extend(["## 岗位分布", "", "| 岗位 | 条数 |", "| --- | ---: |"])
    for position in POSITION_ORDER:
        if position_counts.get(position):
            lines.append(f"| {position} | {position_counts[position]:,} |")
    for position, count in position_counts.most_common():
        if position not in POSITION_ORDER:
            lines.append(f"| {position} | {count:,} |")
    lines.append("")

    lines.extend(["## 本次更新", ""])
    if new_records:
        new_groups = Counter(
            (record.get("company") or "其他公司", record.get("position") or "其他岗位")
            for record in new_records
        )
        lines.append(f"新增 **{new_count:,}** 条，涉及 {len(new_groups):,} 个公司-岗位，增量最多的如下：")
        lines.append("")
        for (company, position), count in new_groups.most_common(20):
            rel_path = os.path.relpath(
                output_dir / _slug(company) / f"{_slug(position)}.md", readme_path.parent
            ).replace(os.sep, "/")
            lines.append(f"- [{company} / {position}]({rel_path})：{count} 条")
        lines.append("")
        lines.append("<details><summary>展开本次新增标题</summary>")
        lines.append("")
        for record in sorted(new_records, key=_record_sort_key, reverse=True)[:30]:
            title = _md_escape(record.get("title") or "未命名面经")
            url = record.get("url") or ""
            company = record.get("company") or "其他公司"
            position = record.get("position") or "其他岗位"
            lines.append(f"- [{title}]({url}) ｜ {company} · {position}")
        lines.append("")
        lines.append("</details>")
        lines.append("")
    else:
        lines.extend(["本次无新增记录，仅刷新索引与文件。", ""])

    lines.extend(
        [
            "## 数据文件",
            "",
            "| 公司 | 岗位 | 条数 | 文件 | 最后更新（UTC+8） |",
            "| --- | --- | ---: | --- | --- |",
            *table_rows,
            "",
            "## 说明",
            "",
            "- 每个 Markdown 文件保存对应公司/岗位的面经正文，正文不再截断。",
            "- 数据来自各站点公开页面，内容版权归原作者所有；每条均保留原文链接。",
            "- 仅收录国内公司，国外公司（含 PracHub 数据）已默认剔除。",
            "- 采集每日增量、每周全量；受站点改版和反爬策略影响，可能出现漏采或延迟。",
            "- 如需调整关键词、页数或数据源，请修改 [config.yaml](config.yaml) 后重新运行。",
            "",
            "## 维护",
            "",
            "- 每日增量：`.github/workflows/daily.yml` 每天 09:00（北京时间）执行。",
            "- 每周全量：`.github/workflows/weekly-full.yml` 每周日 10:00（北京时间）执行 `--full`。",
            "- 本地运行：`pip install -r requirements.txt && python -m src.main --config config.yaml`。",
            "- 只跑单个数据源：`python -m src.main --source nowcoder`。",
            "",
        ]
    )

    _write_if_changed(readme_path, "\n".join(lines))
