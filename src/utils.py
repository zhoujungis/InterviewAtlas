"""通用工具函数。"""

from __future__ import annotations

import hashlib
import html
import re
from datetime import datetime, timedelta, timezone

CST = timezone(timedelta(hours=8))


def clean_text(value: str | None, limit: int | None = None) -> str:
    """压缩空白、去掉 HTML 标签和零宽字符。"""
    if not value:
        return ""
    text = re.sub(r"<[^>]+>", " ", value)
    text = text.replace("\u200b", "").replace("\xa0", " ")
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        return text[: limit - 1].rstrip() + "…"
    return text


def clean_content(value: str | None, limit: int | None = None) -> str:
    """清洗正文但保留段落和换行，供完整面经展示。"""
    if not value:
        return ""
    text = str(value)
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"</(p|div|li|h[1-6])>", "\n\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = text.replace("\u200b", "").replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()
    if limit and len(text) > limit:
        return text[: limit - 1].rstrip() + "…"
    return text


def ms_to_date(value: int | str | None) -> str | None:
    """毫秒时间戳转北京时间日期字符串。"""
    if value in (None, "", 0):
        return None
    try:
        ts = float(value) / 1000
    except (TypeError, ValueError):
        return None
    if ts <= 0:
        return None
    return datetime.fromtimestamp(ts, tz=CST).date().isoformat()


def unix_to_date(value: int | str | None) -> str | None:
    """秒级时间戳转北京时间日期字符串。"""
    if value in (None, "", 0):
        return None
    try:
        ts = float(value)
    except (TypeError, ValueError):
        return None
    if ts <= 0:
        return None
    return datetime.fromtimestamp(ts, tz=CST).date().isoformat()


def today_cst() -> str:
    return datetime.now(CST).date().isoformat()


def now_cst() -> str:
    return datetime.now(CST).strftime("%Y-%m-%d %H:%M")


def digest(*parts: str) -> str:
    raw = "|".join(p for p in parts if p)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]


def slugify(text: str) -> str:
    """把公司/岗位名转成安全的文件名。"""
    value = (text or "未分类").replace("/", "-").replace("\\", "-")
    value = re.sub(r'[<>:"|?*#%\[\]]', "", value).strip(" .")
    return value or "未分类"
