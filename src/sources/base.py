"""数据源基类。"""

from __future__ import annotations

import logging

from ..http import HttpClient

log = logging.getLogger(__name__)


class BaseSource:
    key = "base"
    display_name = ""

    def __init__(self, config: dict, client: HttpClient):
        self.config = config
        self.client = client
        self.full = bool(config.get("_full"))
        self.companies = list(config.get("_companies") or [])
        self.known_urls = set(config.get("_known_urls") or [])
        self.known_content = set(config.get("_known_content") or [])
        self.log = logging.getLogger(f"source.{self.key}")

    def fetch(self) -> list[dict]:
        raise NotImplementedError

    def build_queries(self, defaults: list[str] | None = None) -> list[str]:
        """基础关键词 + 按公司批量生成的「公司 + 面经」关键词。"""
        queries = list(defaults if defaults is not None else (self.config.get("queries") or []))
        key = "full_company_queries" if self.full else "company_queries"
        templates = self.config.get(key) or []
        for company in self.companies:
            for template in templates:
                try:
                    queries.append(template.format(company=company))
                except (KeyError, IndexError):
                    continue

        deduped: list[str] = []
        seen: set[str] = set()
        for query in queries:
            query = query.strip()
            if query and query not in seen:
                seen.add(query)
                deduped.append(query)
        return deduped

    def _item(
        self,
        *,
        external_id: str | int,
        title: str,
        url: str,
        summary: str = "",
        content: str = "",
        published_at: str | None = None,
        company: str = "",
        company_hint: str = "",
        position_hint: str = "",
        query: str = "",
        kind: str = "面经",
        is_experience: bool = False,
    ) -> dict:
        return {
            "source": self.key,
            "source_name": self.display_name,
            "external_id": str(external_id),
            "title": title,
            "url": url,
            "summary": summary,
            "content": content or summary,
            "published_at": published_at,
            "company": company,
            "company_hint": company_hint,
            "position_hint": position_hint,
            "query": query,
            "kind": kind,
            "is_experience": is_experience,
        }
