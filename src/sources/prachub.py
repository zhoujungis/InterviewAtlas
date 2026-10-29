"""PracHub 数据源：解析英文面试经验列表页。"""

from __future__ import annotations

import json
import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from ..utils import clean_text
from .base import BaseSource

BASE = "https://www.prachub.com/interview-experiences"
MONTHS = {
    "jan": "01", "feb": "02", "mar": "03", "apr": "04", "may": "05", "jun": "06",
    "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12",
}


def _parse_added(text: str) -> str | None:
    match = re.search(r"(?:Added\s+)?([A-Za-z]{3})\s+(\d{4})", text)
    if not match:
        return None
    month = MONTHS.get(match.group(1).lower())
    return f"{match.group(2)}-{month}" if month else None


class PrachubSource(BaseSource):
    key = "prachub"
    display_name = "PracHub"

    def fetch(self) -> list[dict]:
        max_pages = int(self.config.get("max_pages", 5))
        results: list[dict] = []
        seen: set[str] = set()

        for page in range(1, max_pages + 1):
            url = BASE if page == 1 else f"{BASE}?page={page}"
            try:
                resp = self.client.get(url)
            except Exception as exc:  # noqa: BLE001
                self.log.warning("PracHub 请求失败 page=%s: %s", page, exc)
                break

            soup = BeautifulSoup(resp.text, "lxml")
            jsonld_meta = self._jsonld_meta(soup)
            cards = soup.select('a[href^="/interview-experiences/"]')
            new_in_page = 0

            for card in cards:
                href = card.get("href", "")
                if "contribute" in href:
                    continue
                absolute = urljoin(BASE, href)
                if absolute in seen:
                    continue
                seen.add(absolute)

                ld_meta = jsonld_meta.get(urlparse(absolute).path, {})
                title_el = card.find("h3")
                title = clean_text(title_el.get_text(" ", strip=True)) if title_el else ""
                if ld_meta.get("name") and len(ld_meta["name"]) > len(title):
                    title = clean_text(ld_meta["name"])
                if not title:
                    continue

                company_el = card.select_one("span.font-semibold")
                company = clean_text(company_el.get_text(" ", strip=True)) if company_el else ""
                company = company or ld_meta.get("company", "")

                role_el = card.select_one("span.text-zinc-500")
                role = clean_text(role_el.get_text(" ", strip=True)) if role_el else ""

                level_el = card.select_one("span.text-violet-600")
                level = clean_text(level_el.get_text(" ", strip=True)) if level_el else ""

                excerpt_el = card.find("p", class_=lambda c: bool(c) and "line-clamp-2" in c)
                excerpt = clean_text(excerpt_el.get_text(" ", strip=True)) if excerpt_el else ""

                date_el = card.find("span", string=re.compile(r"(?:Added\s+)?[A-Za-z]{3}\s+\d{4}"))
                published = _parse_added(date_el.get_text(" ", strip=True)) if date_el else None

                meta = " · ".join(part for part in [role, level] if part)
                summary = f"{meta}. {excerpt}" if meta else excerpt

                results.append(
                    self._item(
                        external_id=absolute.rstrip("/").rsplit("/", 1)[-1],
                        title=title,
                        url=absolute,
                        summary=summary,
                        published_at=published,
                        company=company,
                        position_hint=role,
                        is_experience=True,
                    )
                )
                new_in_page += 1

            self.log.info("PracHub page=%s 解析 %s 条", page, new_in_page)
            if new_in_page == 0:
                break

        return results

    @staticmethod
    def _jsonld_meta(soup: BeautifulSoup) -> dict[str, dict[str, str]]:
        """从 JSON-LD 中建立 path -> {公司, 标题} 映射，作为卡片字段的补充。"""
        mapping: dict[str, dict[str, str]] = {}
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                data = json.loads(script.string or "")
            except (TypeError, json.JSONDecodeError):
                continue
            if not isinstance(data, dict) or data.get("@type") != "ItemList":
                continue
            for entry in data.get("itemListElement") or []:
                item = entry.get("item") if isinstance(entry, dict) else None
                if not isinstance(item, dict) or not item.get("url"):
                    continue
                author = item.get("author") or {}
                name = author.get("name") if isinstance(author, dict) else None
                mapping[urlparse(item["url"]).path] = {
                    "company": name or "",
                    "name": item.get("name") or "",
                }
        return mapping
