"""面试鸭数据源：遍历全部题库，展开题库中的面试题。"""

from __future__ import annotations

from ..normalize import detect_company
from ..utils import clean_text
from .base import BaseSource

BANK_API = "https://api.mianshiya.com/api/question_bank/list/page/vo"
QUESTION_API = "https://api.mianshiya.com/api/question/search"
SITE = "https://www.mianshiya.com"
QUESTION_PAGE_SIZE = 20


class MianshiyaSource(BaseSource):
    key = "mianshiya"
    display_name = "面试鸭"

    def fetch(self) -> list[dict]:
        max_banks = int(self.config.get("max_banks", 400))
        bank_page_size = min(int(self.config.get("page_size", 100)), 100)
        max_question_pages = int(self.config.get("max_question_pages", 10))

        banks: list[dict] = []
        for page in range(1, 12):
            try:
                body = self.client.post_json(
                    BANK_API,
                    {"current": page, "pageSize": bank_page_size},
                    headers={"Referer": "https://www.mianshiya.com/"},
                ).json()
            except Exception as exc:  # noqa: BLE001
                self.log.warning("面试鸭题库列表请求失败 page=%s: %s", page, exc)
                break

            data = body.get("data") or {}
            records = data.get("records") or []
            if not records:
                break
            banks.extend(records)
            total_pages = int(data.get("pages") or 0)
            if (total_pages and page >= total_pages) or len(records) < bank_page_size:
                break

        banks = banks[:max_banks]
        self.log.info("面试鸭共 %s 个题库，开始展开题目", len(banks))

        index: dict[str, dict] = {}
        for idx, bank in enumerate(banks, start=1):
            bank_id = str(bank.get("id") or "")
            bank_title = clean_text(bank.get("title"))
            if not bank_id or not bank_title:
                continue
            company = detect_company(bank_title) or ""
            if not company:
                # 只保留能识别出公司的题库，通用题库会全部落到「其他公司」
                continue
            description = clean_text(bank.get("description"))
            published = str(bank.get("createTime") or "")[:10] or None

            questions = self._fetch_questions(bank_id, max_question_pages)
            if not questions:
                # 题库本身没有题目时，至少保留题库作为一条记录
                self._merge(
                    index,
                    self._item(
                        external_id=f"bank:{bank_id}",
                        title=bank_title,
                        url=f"{SITE}/bank/{bank_id}",
                        summary=description,
                        content=description or bank_title,
                        published_at=published,
                        company=company,
                        company_hint=bank_title,
                        position_hint=bank_title,
                        is_experience=True,
                        kind="题库",
                    ),
                )
                continue

            for question in questions:
                question_id = str(question.get("id") or "")
                question_title = clean_text(question.get("title"))
                if not question_id or not question_title:
                    continue
                content = question_title
                if description and company:
                    content = f"{question_title}\n\n题库：{bank_title}｜{description}"
                else:
                    content = f"{question_title}\n\n题库：{bank_title}"
                self._merge(
                    index,
                    self._item(
                        external_id=question_id,
                        title=question_title,
                        url=f"{SITE}/question/{question_id}",
                        summary=question_title,
                        content=content,
                        published_at=str(question.get("createTime") or "")[:10] or published,
                        company=company,
                        company_hint=bank_title,
                        position_hint=bank_title,
                        is_experience=True,
                        kind="面试题",
                    ),
                )

            if idx % 20 == 0:
                self.log.info(
                    "面试鸭已处理 %s/%s 个题库，累计题目 %s 条", idx, len(banks), len(index)
                )

        self.log.info("面试鸭完成：%s 个题库共 %s 条记录", len(banks), len(index))
        return list(index.values())

    @staticmethod
    def _merge(index: dict[str, dict], item: dict) -> None:
        """同一道题可能出现在多个题库，优先归属到能识别公司的题库。"""
        key = item["external_id"]
        old = index.get(key)
        if old is None:
            index[key] = item
            return
        if (not old.get("company")) and item.get("company"):
            index[key] = item

    def _fetch_questions(self, bank_id: str, max_pages: int) -> list[dict]:
        """题目接口每个查询最多只能翻 5 页，用难度分组绕开单次上限。"""
        questions: list[dict] = []
        seen: set[str] = set()
        variants: list[dict] = [{}, {"difficulty": 1}, {"difficulty": 3}]
        for extra in variants:
            for page in range(1, max_pages + 1):
                try:
                    body = self.client.post_json(
                        QUESTION_API,
                        {
                            "current": page,
                            "pageSize": QUESTION_PAGE_SIZE,
                            "questionBankId": bank_id,
                            **extra,
                        },
                        headers={"Referer": f"{SITE}/bank/{bank_id}"},
                    ).json()
                except Exception as exc:  # noqa: BLE001
                    self.log.warning("面试鸭题目请求失败 bank=%s page=%s: %s", bank_id, page, exc)
                    break
                data = body.get("data") or {}
                records = data.get("records") or []
                for record in records:
                    question_id = str(record.get("id") or "")
                    if question_id and question_id not in seen:
                        seen.add(question_id)
                        questions.append(record)
                total_pages = int(data.get("pages") or 0)
                if (
                    not records
                    or len(records) < QUESTION_PAGE_SIZE
                    or (total_pages and page >= total_pages)
                ):
                    break
        return questions
