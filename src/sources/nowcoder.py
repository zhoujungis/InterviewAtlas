"""牛客网数据源：搜索接口发现面经，再用详情接口补全正文。"""

from __future__ import annotations

import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

from ..utils import clean_content, clean_text, ms_to_date
from .base import BaseSource

API = "https://gw-c.nowcoder.com/api/sparta/pc/search"
DETAIL_API = "https://gw-c.nowcoder.com/api/sparta/detail/{kind}-data/detail/{cid}"


def _rich_text(value) -> str:
    """把牛客的富文本结构转成纯文本。"""
    if isinstance(value, str):
        return value
    if not isinstance(value, dict):
        return ""
    parts = value.get("data") or []
    return "\n".join(
        str(part.get("text", "")) for part in parts if isinstance(part, dict) and part.get("text")
    )


def _pick_body(node: dict) -> str:
    """优先取较长的正文，搜索接口会截断，详情接口才完整。"""
    plain = node.get("content") or ""
    rich = _rich_text(node.get("newContent"))
    plain_text = clean_content(plain if isinstance(plain, str) else "")
    rich_text = clean_content(rich)
    return rich_text if len(rich_text) > len(plain_text) else plain_text


class NowcoderSource(BaseSource):
    key = "nowcoder"
    display_name = "牛客网"

    def __init__(self, config: dict, client) -> None:
        super().__init__(config, client)
        self.fetch_content = bool(config.get("fetch_content", True))
        self.detail_workers = max(1, int(config.get("detail_workers", 6)))
        self.detail_delay = max(0.0, float(config.get("detail_delay", 0.2)))
        self.detail_limit = int(config.get("detail_limit", 0))
        self._cache: dict[tuple[str, str], str] = {}
        self._cache_lock = threading.Lock()
        self._local = threading.local()

    # -- 详情抓取 ---------------------------------------------------------
    def _session(self) -> requests.Session:
        session = getattr(self._local, "session", None)
        if session is None:
            session = requests.Session()
            session.headers.update(
                {
                    "User-Agent": self.client.session.headers.get("User-Agent", "Mozilla/5.0"),
                    "Referer": "https://www.nowcoder.com/",
                }
            )
            self._local.session = session
            self._local.last = 0.0
        return session

    def _fetch_detail(self, kind: str, cid: str) -> str:
        key = (kind, cid)
        with self._cache_lock:
            cached = self._cache.get(key)
        if cached is not None:
            return cached

        session = self._session()
        elapsed = time.monotonic() - getattr(self._local, "last", 0.0)
        if elapsed < self.detail_delay:
            time.sleep(self.detail_delay - elapsed)
        self._local.last = time.monotonic()

        content = ""
        try:
            resp = session.get(DETAIL_API.format(kind=kind, cid=cid), timeout=self.client.timeout)
            payload = resp.json()
            if payload.get("success"):
                data = payload.get("data") or {}
                content = _pick_body(data)
        except Exception as exc:  # noqa: BLE001
            self.log.warning("牛客详情失败 kind=%s cid=%s: %s", kind, cid, exc)

        with self._cache_lock:
            self._cache[key] = content
        return content

    def _enrich(self, items: list[dict]) -> None:
        if not self.fetch_content:
            for item in items:
                item.pop("_detail", None)
            return

        targets = [
            item
            for item in items
            if item.get("_detail") and item["url"] not in self.known_content
        ]
        if self.detail_limit > 0:
            targets = targets[: self.detail_limit]
        if not targets:
            for item in items:
                item.pop("_detail", None)
            return

        self.log.info("牛客准备补全 %s 条正文（并发 %s）", len(targets), self.detail_workers)
        done = 0
        with ThreadPoolExecutor(max_workers=self.detail_workers) as pool:
            futures = {
                pool.submit(self._fetch_detail, item["_detail"][0], item["_detail"][1]): item
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
                if done % 200 == 0:
                    self.log.info("牛客正文补全进度 %s/%s", done, len(targets))

        for item in items:
            item.pop("_detail", None)

    # -- 搜索 -------------------------------------------------------------
    def fetch(self) -> list[dict]:
        max_pages = int(self.config.get("max_pages", 3))
        page_size = int(self.config.get("page_size", 20))
        queries = self.build_queries(["面经"])

        results: list[dict] = []
        seen: set[str] = set()

        for query in queries:
            for page in range(1, max_pages + 1):
                try:
                    resp = self.client.post_json(
                        API,
                        {"query": query, "type": "post", "page": page, "pageSize": page_size},
                        headers={"Referer": "https://www.nowcoder.com/search"},
                    )
                    payload = resp.json()
                except (ValueError, json.JSONDecodeError):
                    self.log.warning("牛客返回非 JSON，跳过 query=%s page=%s", query, page)
                    break
                except Exception as exc:  # noqa: BLE001
                    self.log.warning("牛客请求失败 query=%s page=%s: %s", query, page, exc)
                    break

                data = payload.get("data") or {}
                records = data.get("records") or []
                if not records:
                    break

                new_in_page = 0
                for record in records:
                    item = self._parse_record(record, query)
                    if not item or item["url"] in seen:
                        continue
                    seen.add(item["url"])
                    results.append(item)
                    new_in_page += 1

                self.log.info(
                    "牛客 query=%s page=%s 获取 %s 条（新增 %s）",
                    query,
                    page,
                    len(records),
                    new_in_page,
                )
                if len(records) < page_size:
                    break

        self.log.info("牛客搜索完成：%s 条，开始补全正文", len(results))
        self._enrich(results)
        return results

    def _parse_record(self, record: dict, query: str) -> dict | None:
        moment = record.get("momentData")
        content = record.get("contentData")

        if isinstance(moment, dict) and (moment.get("title") or moment.get("content") or moment.get("newContent")):
            title = clean_text(moment.get("title") or _rich_text(moment.get("newTitle")))
            body = _pick_body(moment)
            if not title and body:
                title = body[:40]
            uuid = moment.get("uuid") or ""
            moment_id = str(moment.get("id") or "")
            if uuid:
                url = f"https://www.nowcoder.com/feed/main/detail/{uuid}"
                detail = ("moment", uuid)
            else:
                url = f"https://www.nowcoder.com/discuss/{moment_id}"
                detail = ("content", moment_id)
            return self._item(
                external_id=moment_id or uuid,
                title=title,
                url=url,
                summary=clean_text(body, limit=200),
                content=body,
                published_at=ms_to_date(moment.get("createdAt")),
                company_hint=query,
                query=query,
            ) | {"_detail": detail}

        if isinstance(content, dict) and (
            content.get("title") or content.get("content") or content.get("newContent")
        ):
            title = clean_text(content.get("title") or _rich_text(content.get("newTitle")))
            body = _pick_body(content)
            if not title and body:
                title = body[:40]
            cid = str(content.get("id") or "")
            if not cid:
                return None
            return self._item(
                external_id=cid,
                title=title,
                url=f"https://www.nowcoder.com/discuss/{cid}",
                summary=clean_text(body, limit=200),
                content=body,
                published_at=ms_to_date(content.get("createTime")),
                company_hint=query,
                query=query,
            ) | {"_detail": ("content", cid)}

        return None
