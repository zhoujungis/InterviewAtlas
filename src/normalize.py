"""公司 / 岗位归一化与面经相关性判断。"""

from __future__ import annotations

import re

from .utils import clean_content, clean_text

# ---------------------------------------------------------------------------
# 公司别名 -> 统一名称（越长越优先匹配，避免「阿里」抢先匹配「阿里云」）
# ---------------------------------------------------------------------------
COMPANY_ALIASES: dict[str, list[str]] = {
    "字节跳动": ["字节跳动", "字节", "bytedance", "tiktok", "抖音"],
    "腾讯": ["腾讯", "tencent"],
    "腾讯云": ["腾讯云"],
    "腾讯音乐": ["腾讯音乐", "tme"],
    "阿里巴巴": ["阿里巴巴", "阿里", "alibaba", "淘天", "淘宝", "天猫"],
    "阿里云": ["阿里云", "alibaba cloud"],
    "蚂蚁集团": ["蚂蚁集团", "蚂蚁", "ant group", "支付宝"],
    "美团": ["美团", "meituan", "大众点评"],
    "京东": ["京东", "jd.com", "jd"],
    "百度": ["百度", "baidu"],
    "快手": ["快手", "kuaishou"],
    "网易": ["网易", "netease", "网易游戏", "网易云音乐"],
    "拼多多": ["拼多多", "pinduoduo", "pdd", "temu"],
    "MetaApp": ["metaapp", "meta app"],
    "华为": ["华为", "huawei"],
    "华为云": ["华为云"],
    "小米": ["小米", "xiaomi", "redmi"],
    "滴滴": ["滴滴", "didi", "滴滴出行"],
    "小红书": ["小红书", "xiaohongshu", "rednote"],
    "哔哩哔哩": ["哔哩哔哩", "bilibili", "b站"],
    "携程": ["携程", "trip.com", "ctrip"],
    "得物": ["得物", "poizon", "dewu"],
    "希音": ["希音", "shein"],
    "虾皮": ["虾皮", "shopee"],
    "大疆": ["大疆", "dji"],
    "蔚来": ["蔚来", "nio"],
    "理想汽车": ["理想汽车", "理想", "li auto"],
    "小鹏汽车": ["小鹏汽车", "小鹏", "xpeng"],
    "比亚迪": ["比亚迪", "byd"],
    "宁德时代": ["宁德时代", "catl"],
    "OPPO": ["oppo"],
    "vivo": ["vivo"],
    "荣耀": ["荣耀", "honor"],
    "中兴": ["中兴", "zte"],
    "联想": ["联想", "lenovo"],
    "用友": ["用友", "yonyou"],
    "多益网络": ["多益网络", "多益"],
    "金蝶": ["金蝶", "kingdee"],
    "深信服": ["深信服", "sangfor"],
    "奇安信": ["奇安信", "qianxin"],
    "360": ["奇虎360", "360"],
    "货拉拉": ["货拉拉", "lalamove"],
    "贝壳": ["贝壳找房", "贝壳"],
    "爱奇艺": ["爱奇艺", "iqiyi"],
    "知乎": ["知乎", "zhihu"],
    "微博": ["微博", "weibo"],
    "虎牙": ["虎牙", "huya"],
    "斗鱼": ["斗鱼", "douyu"],
    "金山": ["金山", "kingsoft", "wps"],
    "米哈游": ["米哈游", "mihoyo", "hoyoverse"],
    "莉莉丝": ["莉莉丝", "lilith"],
    "完美世界": ["完美世界"],
    "搜狐": ["搜狐", "sohu"],
    "新浪": ["新浪", "sina"],
    "58同城": ["58同城"],
    "去哪儿": ["去哪儿", "qunar"],
    "盒马": ["盒马", "freshippo"],
    "瑞幸": ["瑞幸", "luckin"],
    "美图": ["美图", "meitu"],
    "顺丰": ["顺丰", "sf express"],
    "中国平安": ["中国平安", "平安"],
    "招商银行": ["招商银行", "招行"],
    "工商银行": ["工商银行", "工行"],
    "建设银行": ["建设银行", "建行"],
    "中国银行": ["中国银行", "中行"],
    "农业银行": ["农业银行", "农行"],
    "交通银行": ["交通银行", "交行"],
    "中信证券": ["中信证券"],
    "中金公司": ["中金公司", "中金"],
    "中国移动": ["中国移动"],
    "中国电信": ["中国电信"],
    "中国联通": ["中国联通"],
    "微软": ["微软", "microsoft"],
    "谷歌": ["谷歌", "google", "alphabet"],
    "苹果": ["苹果", "apple"],
    "亚马逊": ["亚马逊", "amazon", "aws"],
    "Meta": ["meta", "facebook"],
    "奈飞": ["奈飞", "netflix"],
    "英伟达": ["英伟达", "nvidia"],
    "特斯拉": ["特斯拉", "tesla"],
    "英特尔": ["英特尔", "intel"],
    "高通": ["高通", "qualcomm"],
    "三星": ["三星", "samsung"],
    "甲骨文": ["甲骨文", "oracle"],
    "IBM": ["ibm"],
    "OpenAI": ["openai"],
    "Stripe": ["stripe"],
    "优步": ["优步", "uber"],
    "爱彼迎": ["爱彼迎", "airbnb"],
    "Coinbase": ["coinbase"],
    "DoorDash": ["doordash"],
    "Instacart": ["instacart"],
    "Atlys": ["atlys"],
    "Rippling": ["rippling"],
    "PlayStation": ["playstation", "索尼", "sony"],
    "Pinterest": ["pinterest"],
    "Reddit": ["reddit"],
    "Spotify": ["spotify"],
    "PayPal": ["paypal"],
    "Visa": ["visa"],
    "高盛": ["高盛", "goldman sachs", "goldman"],
    "摩根大通": ["摩根大通", "jpmorgan", "jp morgan"],
    "彭博": ["彭博", "bloomberg"],
    "Databricks": ["databricks"],
    "Snowflake": ["snowflake"],
    "Palantir": ["palantir"],
    "Capital One": ["capital one"],
    "Salesforce": ["salesforce"],
    "Adobe": ["adobe"],
    "领英": ["领英", "linkedin"],
    "Snap": ["snap", "snapchat"],
    "Dropbox": ["dropbox"],
    "思科": ["思科", "cisco"],
    "戴尔": ["戴尔", "dell"],
    "Lyft": ["lyft"],
    "Robinhood": ["robinhood"],
    "Datadog": ["datadog"],
    "Cloudflare": ["cloudflare"],
    "Shopify": ["shopify"],
    "Twitter": ["twitter"],
    "Grab": ["grab"],
    "乐天": ["乐天", "rakuten"],
    "Naver": ["naver"],
    "Kakao": ["kakao"],
    "博世": ["博世", "bosch"],
    "西门子": ["西门子", "siemens"],
    "ARM": ["arm"],
    "AMD": ["amd"],
    "美光": ["美光", "micron"],
    "台积电": ["台积电", "tsmc"],
    "中芯国际": ["中芯国际", "smic"],
    "科大讯飞": ["科大讯飞", "iflytek", "讯飞"],
    "商汤": ["商汤", "sensetime"],
    "旷视": ["旷视", "megvii"],
    "第四范式": ["第四范式", "4paradigm"],
    "深度求索": ["深度求索", "deepseek"],
    "月之暗面": ["月之暗面", "moonshot", "kimi"],
    "智谱AI": ["智谱ai", "智谱", "zhipu"],
    "MiniMax": ["minimax"],
    "海康威视": ["海康威视", "海康", "hikvision"],
    "大华股份": ["大华股份", "大华", "dahua"],
    "新华三": ["新华三", "h3c"],
    "锐捷网络": ["锐捷网络", "锐捷", "ruijie"],
    "浪潮": ["浪潮", "inspur"],
    "紫光": ["紫光", "unigroup"],
    "TCL": ["tcl"],
    "美的": ["美的集团", "美的", "midea"],
    "格力": ["格力", "gree"],
    "海尔": ["海尔", "haier"],
    "富士康": ["富士康", "foxconn"],
    "工业富联": ["工业富联"],
    "立讯精密": ["立讯精密", "立讯", "luxshare"],
    "歌尔股份": ["歌尔股份", "歌尔", "goertek"],
    "蓝思科技": ["蓝思科技", "蓝思"],
    "舜宇光学": ["舜宇光学", "舜宇", "sunny optical"],
    "海思": ["海思", "hisilicon"],
    "韦尔股份": ["韦尔股份", "韦尔"],
    "兆易创新": ["兆易创新", "兆易"],
    "汇顶科技": ["汇顶科技", "汇顶", "goodix"],
    "卓胜微": ["卓胜微", "maxscend"],
    "地平线": ["地平线", "horizon robotics"],
    "寒武纪": ["寒武纪", "cambricon"],
    "依图科技": ["依图科技", "依图", "yitu"],
    "云从科技": ["云从科技", "云从", "cloudwalk"],
    "小马智行": ["小马智行", "pony.ai"],
    "文远知行": ["文远知行", "weride"],
    "禾赛科技": ["禾赛科技", "禾赛", "hesai"],
    "速腾聚创": ["速腾聚创", "速腾", "robosense"],
    "亿咖通": ["亿咖通", "ecarx"],
    "斑马网络": ["斑马网络", "斑马", "banma"],
    "欣旺达": ["欣旺达", "sunwoda"],
    "阳光电源": ["阳光电源", "sungrow"],
    "隆基绿能": ["隆基绿能", "隆基", "longi"],
    "三一重工": ["三一重工", "sany"],
    "中联重科": ["中联重科", "zoomlion"],
    "徐工": ["徐工", "xcmg"],
    "潍柴动力": ["潍柴动力", "潍柴", "weichai"],
    "中国邮政": ["中国邮政", "邮政"],
    "国家电网": ["国家电网", "国网"],
    "中石油": ["中石油", "中国石油"],
    "中石化": ["中石化", "中国石化"],
    "中国建筑": ["中国建筑", "中建"],
    "中国中铁": ["中国中铁", "中铁"],
    "中软国际": ["中软国际", "中软", "chinasoft"],
    "软通动力": ["软通动力", "软通", "isoftstone"],
    "文思海辉": ["文思海辉", "pactera"],
    "烽火通信": ["烽火通信", "烽火", "fiberhome"],
    "大唐电信": ["大唐电信", "大唐"],
    "迈瑞医疗": ["迈瑞医疗", "迈瑞", "mindray"],
    "药明康德": ["药明康德", "药明", "wuxi apptec"],
    "兴业银行": ["兴业银行", "兴业"],
    "浦发银行": ["浦发银行", "浦发"],
    "民生银行": ["民生银行", "民生"],
    "光大银行": ["光大银行", "光大"],
    "华夏银行": ["华夏银行"],
    "广发银行": ["广发银行", "广发"],
    "平安银行": ["平安银行"],
    "中国人寿": ["中国人寿", "国寿"],
    "中国人保": ["中国人保", "人保"],
    "中信建投": ["中信建投", "建投"],
    "华泰证券": ["华泰证券", "华泰"],
    "国泰君安": ["国泰君安", "国君"],
    "东方财富": ["东方财富", "东财"],
    "同花顺": ["同花顺", "hithink"],
    "猿辅导": ["猿辅导", "yuanfudao"],
    "作业帮": ["作业帮", "zuoyebang"],
    "好未来": ["好未来", "学而思"],
    "新东方": ["新东方", "xdf"],
    "网易有道": ["网易有道", "有道", "youdao"],
    "喜马拉雅": ["喜马拉雅", "ximalaya"],
    "饿了么": ["饿了么", "ele.me", "eleme"],
    "闲鱼": ["闲鱼"],
    "飞猪": ["飞猪", "fliggy"],
    "钉钉": ["钉钉", "dingtalk"],
    "中小公司": ["中小公司", "中小厂", "小公司", "小厂"],
}

# 国外公司：默认从结果中剔除（可通过 config.yaml 的 exclude_foreign_companies 关闭）
FOREIGN_COMPANIES: set[str] = {
    "微软",
    "谷歌",
    "苹果",
    "亚马逊",
    "Meta",
    "奈飞",
    "英伟达",
    "特斯拉",
    "英特尔",
    "高通",
    "三星",
    "甲骨文",
    "IBM",
    "OpenAI",
    "Stripe",
    "优步",
    "爱彼迎",
    "Coinbase",
    "DoorDash",
    "Instacart",
    "Atlys",
    "Rippling",
    "PlayStation",
    "Pinterest",
    "Reddit",
    "Spotify",
    "PayPal",
    "Visa",
    "高盛",
    "摩根大通",
    "彭博",
    "Databricks",
    "Snowflake",
    "Palantir",
    "Capital One",
    "Salesforce",
    "Adobe",
    "领英",
    "Snap",
    "Dropbox",
    "思科",
    "戴尔",
    "Lyft",
    "Robinhood",
    "Datadog",
    "Cloudflare",
    "Shopify",
    "Twitter",
    "Grab",
    "乐天",
    "Naver",
    "Kakao",
    "博世",
    "西门子",
    "ARM",
    "AMD",
    "美光",
}


def is_foreign_company(company: str | None) -> bool:
    return (company or "") in FOREIGN_COMPANIES


# 展平成 (别名小写, 统一名称)，按长度倒序匹配
_ALIAS_INDEX: list[tuple[str, str]] = sorted(
    ((alias.lower(), canonical) for canonical, aliases in COMPANY_ALIASES.items() for alias in aliases),
    key=lambda item: len(item[0]),
    reverse=True,
)

_ASCII_ALIAS_RE = {
    alias: re.compile(r"(?<![a-z0-9])" + re.escape(alias) + r"(?![a-z0-9])")
    for alias, _ in _ALIAS_INDEX
    if alias.isascii()
}

# ---------------------------------------------------------------------------
# 岗位分类规则（顺序即优先级）
# ---------------------------------------------------------------------------
POSITION_RULES: list[tuple[str, list[str]]] = [
    (
        "算法/AI",
        [
            "大模型",
            "多模态",
            "机器学习",
            "深度学习",
            "人工智能",
            "算法",
            "推荐",
            "搜索",
            "数据挖掘",
            "nlp",
            "计算机视觉",
            "llm",
            "aigc",
            "agent",
            "machine learning",
            "deep learning",
            "research scientist",
            "ai engineer",
            "ai岗",
            "ai应用",
            "ai开发",
        ],
    ),
    ("前端", ["前端", "frontend", "front-end", "front end", "react", "vue", "web开发", "web前端", "h5"]),
    ("客户端", ["客户端", "android", "安卓", "ios", "鸿蒙", "harmonyos", "flutter", "移动开发", "mobile engineer"]),
    ("测试", ["测试开发", "测试工程师", "软件测试", "自动化测试", "测开", "测试", "qa", "sdet", "test engineer"]),
    (
        "数据",
        ["数据开发", "数据仓库", "数仓", "大数据", "大数据开发", "数据分析", "数据挖掘", "数开", "数分", "data engineer", "data scientist", "data analyst", "etl", "bi工程师"],
    ),
    ("运维/SRE", ["运维", "sre", "devops", "site reliability", "云原生", "kubernetes", "k8s", "系统工程师"]),
    ("安全", ["安全工程师", "网络安全", "信息安全", "渗透测试", "security engineer", "安全"]),
    ("嵌入式/硬件", ["嵌入式", "单片机", "驱动开发", "硬件", "fpga", "firmware", "hardware", "embedded", "芯片"]),
    ("游戏", ["游戏", "unity", "unreal", "ue4", "ue5", "引擎开发", "game"]),
    ("产品", ["产品经理", "产品岗", "产品专家", "产品运营", "产品面经", "product manager", "product owner"]),
    ("运营", ["运营", "operation"]),
    ("设计", ["ui设计", "交互设计", "视觉设计", "设计师", "ux", "designer"]),
    ("全栈", ["全栈", "full stack", "fullstack", "full-stack"]),
    ("后端", ["后端", "服务端", "java", "golang", "go开发", "c++", "cpp", "python", "php", ".net", "spring", "backend", "back-end", "back end", "server engineer"]),
    (
        "软件工程师",
        ["软件开发", "软件工程师", "研发工程师", "software engineer", "software developer", "sde", "software development engineer", "new grad"],
    ),
]

POSITION_ORDER = [
    "后端",
    "前端",
    "客户端",
    "算法/AI",
    "数据",
    "测试",
    "运维/SRE",
    "安全",
    "嵌入式/硬件",
    "游戏",
    "产品",
    "运营",
    "设计",
    "全栈",
    "软件工程师",
    "其他岗位",
]

# 摘要中的岗位词更严格，避免「测试一下」「这个产品」之类的泛词误标
POSITION_STRONG: list[tuple[str, list[str]]] = [
    (
        "算法/AI",
        ["算法工程师", "算法岗", "机器学习", "深度学习", "大模型", "nlp", "计算机视觉", "推荐算法", "搜索算法", "ai工程师", "ai岗"],
    ),
    ("前端", ["前端开发", "前端工程师", "web前端", "frontend engineer", "frontend developer"]),
    ("客户端", ["客户端开发", "客户端工程师", "android开发", "ios开发", "安卓开发", "移动端开发"]),
    ("测试", ["测试开发", "测试工程师", "软件测试", "自动化测试", "测开", "qa工程师", "sdet", "test engineer"]),
    ("数据", ["数据开发", "数据工程师", "数据分析", "数据仓库", "大数据开发", "data engineer", "data scientist", "data analyst"]),
    ("运维/SRE", ["运维工程师", "sre", "devops", "云原生", "site reliability"]),
    ("安全", ["安全工程师", "网络安全", "信息安全", "渗透测试", "security engineer"]),
    ("嵌入式/硬件", ["嵌入式开发", "嵌入式软件", "硬件工程师", "驱动开发", "fpga"]),
    ("游戏", ["游戏开发", "游戏客户端", "unity开发", "引擎开发"]),
    ("产品", ["产品经理", "产品岗", "产品专家", "产品运营", "产品实习", "product manager", "product owner"]),
    ("运营", ["运营专员", "运营经理", "用户运营", "内容运营", "活动运营", "电商运营"]),
    ("设计", ["ui设计", "交互设计", "视觉设计", "设计师"]),
    ("全栈", ["全栈工程师", "full stack", "fullstack"]),
    ("后端", ["后端开发", "后端工程师", "服务端开发", "java开发", "golang开发", "c++开发", "python开发", "backend engineer", "backend developer"]),
    ("软件工程师", ["软件工程师", "软件开发工程师", "研发工程师", "software engineer", "software developer", "sde"]),
]

# 面经相关性：标题/摘要必须命中其一
_EXPERIENCE_STRONG = [
    "面经",
    "面试经验",
    "面试经历",
    "面试记录",
    "面试总结",
    "面试复盘",
    "面试分享",
    "面试过程",
    "面试流程",
    "面试凉经",
    "凉经",
    "面完",
    "面后感",
    "interview experience",
]

_EXPERIENCE_WEAK = ["经验", "经历", "记录", "总结", "复盘", "分享", "流程", "过程"]


def _alias_position(text: str, alias: str) -> int:
    """别名在文本中的位置，找不到返回 -1。"""
    if alias.isascii():
        pattern = _ASCII_ALIAS_RE.get(alias)
        found = pattern.search(text) if pattern else None
        return found.start() if found else -1
    return text.find(alias)


def detect_company(text: str | None) -> str | None:
    """从文本中识别公司，优先取最早出现的公司，同一位置取更长别名。"""
    if not text:
        return None
    low = clean_text(text).lower()
    if not low:
        return None

    best: tuple[tuple[int, int], str] | None = None
    for alias, canonical in _ALIAS_INDEX:
        pos = _alias_position(low, alias)
        if pos < 0:
            continue
        score = (pos, -len(alias))
        if best is None or score < best[0]:
            best = (score, canonical)
    return best[1] if best else None


def _match_keyword(low: str, keyword: str) -> bool:
    if keyword.isascii():
        return bool(re.search(r"(?<![a-z0-9])" + re.escape(keyword) + r"(?![a-z0-9])", low))
    return keyword in low


def detect_position(text: str | None) -> str | None:
    """从文本中识别岗位方向。"""
    if not text:
        return None
    low = clean_text(text).lower()
    if not low:
        return None
    for label, keywords in POSITION_RULES:
        for keyword in keywords:
            if _match_keyword(low, keyword):
                return label
    return None


def detect_position_strict(text: str | None) -> str | None:
    """摘要场景使用：只认明确的岗位短语。"""
    if not text:
        return None
    low = clean_text(text).lower()
    if not low:
        return None
    for label, keywords in POSITION_STRONG:
        for keyword in keywords:
            if _match_keyword(low, keyword):
                return label
    return None


def _is_truncated(content: str) -> bool:
    """只有摘要且以省略号结尾的短内容，视为抓取失败，不再入库。"""
    return len(content) < 300 and content.rstrip().endswith("…")


def is_interview_experience(title: str, summary: str = "") -> bool:
    """判断内容是否是「面试经验」而非普通面试题/招聘信息。"""
    text = f"{title} {summary}".lower()
    if any(k in text for k in _EXPERIENCE_STRONG):
        return True
    if "面试" in text and any(k in text for k in _EXPERIENCE_WEAK):
        return True
    if re.search(r"[一二三四五六七八九十]面", text):
        return True
    return False


def normalize_record(raw: dict) -> dict | None:
    """把各数据源的原始条目归一化为统一结构，非面经返回 None。"""
    title = clean_text(raw.get("title"))
    if not title:
        return None

    content = clean_content(raw.get("content") or raw.get("summary") or "")
    summary = clean_text(content, limit=200)
    if _is_truncated(content):
        return None
    if not raw.get("is_experience") and not is_interview_experience(title, content[:500]):
        return None

    explicit_company = clean_text(raw.get("company"))

    company = detect_company(explicit_company) or explicit_company
    if not company:
        company = detect_company(title) or detect_company(summary[:160])
    if not company:
        hint_company = detect_company(clean_text(raw.get("company_hint") or raw.get("query")))
        if hint_company and not is_foreign_company(hint_company):
            company = hint_company
    company = company or "其他公司"

    position = (
        detect_position(title)
        or detect_position_strict(content[:400])
        or clean_text(raw.get("position_hint"))
        or "其他岗位"
    )
    if position not in POSITION_ORDER:
        position = detect_position(position) or "其他岗位"

    url = (raw.get("url") or "").strip()
    if not url.startswith("http"):
        return None

    return {
        "id": raw.get("id") or "",
        "source": raw.get("source", ""),
        "external_id": str(raw.get("external_id") or ""),
        "title": title,
        "url": url,
        "company": company,
        "position": position,
        "content": content,
        "kind": raw.get("kind") or "面经",
        "published_at": raw.get("published_at"),
        "first_seen": raw.get("first_seen"),
        "last_seen": raw.get("last_seen"),
    }


def refresh_record(record: dict) -> dict | None:
    """用最新的归一化规则重算历史记录的公司与岗位（不重新判断相关性）。"""
    title = clean_text(record.get("title"))
    if not title:
        return None
    content = clean_content(record.get("content") or record.get("summary") or "")
    if _is_truncated(content):
        return None
    summary = clean_text(content, limit=200)

    refreshed = dict(record)
    refreshed["title"] = title
    refreshed["content"] = content
    refreshed.pop("summary", None)
    refreshed["kind"] = record.get("kind") or "面经"
    refreshed["company"] = (
        detect_company(title)
        or detect_company(summary[:160])
        or record.get("company")
        or "其他公司"
    )
    old_position = record.get("position")
    refreshed["position"] = (
        detect_position(title)
        or detect_position_strict(content[:400])
        or (old_position if old_position in POSITION_ORDER else "其他岗位")
    )
    return refreshed
