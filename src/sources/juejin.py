"""掘金数据源：搜索接口发现文章，再抓文章 HTML 中的完整正文。"""

from __future__ import annotations

import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import quote

import requests

from ..utils import clean_content, clean_text, unix_to_date
from .base import BaseSource

API = "https://api.juejin.cn/search_api/v1/search"


def _extract_embedded(html_text: str) -> str:
    """掘金文章页把正文放在 web_html_content / mark_content 的转义字符串里。"""
    for marker in ('web_html_content:"', 'mark_content:"'):
        idx = html_text.find(marker)
        if idx >= 0:
            break
    else:
        return ""
    start = idx + len(marker)
    chars: list[str] = []
    escaped = False
    for char in html_text[start:]:
        if escaped:
            chars.append(char)
            escaped = False
        elif char == "\\":
            chars.append(char)
            escaped = True
        elif char == '"':
            break
        else:
            chars.append(char)
    raw = "".join(chars)
    try:
        return json.loads('"' + raw + '"')
    except (json.JSONDecodeError, ValueError):
        return raw.replace("\\n", "\n").replace('\\"', '"')


class JuejinSource(BaseSource):
    key = "juejin"
    display_name = "掘金"

    def __init__(self, config: dict, client) -> None:
        super().__init__(config, client)
        self.fetch_content = bool(config.get("fetch_content", True))
        self.detail_workers = max(1, int(config.get("detail_workers", 6)))
        self.detail_delay = max(0.0, float(config.get("detail_delay", 0.2)))
        self.detail_limit = int(config.get("detail_limit", 0))
        self._cache: dict[str, str] = {}
        self._cache_lock = threading.Lock()
        self._local = threading.local()

    def _session(self) -> requests.Session:
        session = getattr(self._local, "session", None)
        if session is None:
            session = requests.Session()
            session.headers.update(
                {
                    "User-Agent": self.client.session.headers.get("User-Agent", "Mozilla/5.0"),
                    "Referer": "https://juejin.cn/",
                }
            )
            self._local.session = session
            self._local.last = 0.0
        return session

    def _fetch_article_content(self, article_id: str) -> str:
        with self._cache_lock:
            cached = self._cache.get(article_id)
        if cached is not None:
            return cached

        session = self._session()
        elapsed = time.monotonic() - getattr(self._local, "last", 0.0)
        if elapsed < self.detail_delay:
            time.sleep(self.detail_delay - elapsed)
        self._local.last = time.monotonic()

        content = ""
        try:
            resp = session.get(f"https://juejin.cn/post/{article_id}", timeout=self.client.timeout)
            content = clean_content(_extract_embedded(resp.text))
        except Exception as exc:  # noqa: BLE001
            self.log.warning("掘金正文获取失败 article=%s: %s", article_id, exc)

        with self._cache_lock:
            self._cache[article_id] = content
        return content

    def _enrich(self, items: list[dict]) -> None:
        if not self.fetch_content:
            for item in items:
                item.pop("_article_id", None)
            return

        targets = [item for item in items if item["url"] not in self.known_content]
        if self.detail_limit > 0:
            targets = targets[: self.detail_limit]
        if not targets:
            for item in items:
                item.pop("_article_id", None)
            return

        self.log.info("掘金准备抓取 %s 篇正文（并发 %s）", len(targets), self.detail_workers)
        done = 0
        with ThreadPoolExecutor(max_workers=self.detail_workers) as pool:
            futures = {
                pool.submit(self._fetch_article_content, item["_article_id"]): item
                for item in targets
            }
            for future in as_completed(futures):
                item = futures[future]
                try:
                    content = future.result()
                except Exception:  # noqa: BLE001
                    content = ""
                if content:
                    item["content"] = content
                    item["summary"] = clean_text(content, limit=200)
                done += 1
                if done % 100 == 0:
                    self.log.info("掘金正文抓取进度 %s/%s", done, len(targets))

        for item in items:
            item.pop("_article_id", None)

    def fetch(self) -> list[dict]:
        max_pages = int(self.config.get("max_pages", 2))
        queries = self.build_queries(["面经"])

        results: list[dict] = []
        seen: set[str] = set()

        for query in queries:
            cursor = "0"
            for page in range(1, max_pages + 1):
                payload = {
                    "key_word": query,
                    "id_type": 0,
                    "cursor": cursor,
                    "limit": 20,
                    "search_type": 0,
                }
                try:
                    resp = self.client.post_json(
                        API,
                        payload,
                        headers={
                            "Referer": f"https://juejin.cn/search?query={quote(query)}",
                            "Origin": "https://juejin.cn",
                        },
                    )
                    data = resp.json()
                except Exception as exc:  # noqa: BLE001
                    self.log.warning("掘金请求失败 query=%s page=%s: %s", query, page, exc)
                    break

                items = data.get("data") or []
                new_in_page = 0
                for entry in items:
                    model = entry.get("result_model") if isinstance(entry, dict) else None
                    info = (model or {}).get("article_info") if isinstance(model, dict) else None
                    if not isinstance(info, dict):
                        continue
                    article_id = str(info.get("article_id") or "")
                    if not article_id:
                        continue
                    url = f"https://juejin.cn/post/{article_id}"
                    if url in seen:
                        continue
                    seen.add(url)
                    brief = clean_text(info.get("brief_content"))
                    results.append(
                        self._item(
                            external_id=article_id,
                            title=clean_text(info.get("title")),
                            url=url,
                            summary=brief,
                            content=brief,
                            published_at=unix_to_date(info.get("ctime")),
                            company_hint=query,
                            query=query,
                        )
                        | {"_article_id": article_id}
                    )
                    new_in_page += 1

                self.log.info(
                    "掘金 query=%s page=%s 获取 %s 条（新增 %s）",
                    query,
                    page,
                    len(items),
                    new_in_page,
                )
                cursor = data.get("cursor") or ""
                if not items or not data.get("has_more") or not cursor:
                    break

        self.log.info("掘金搜索完成：%s 条，开始抓取正文", len(results))
        self._enrich(results)
        return results
