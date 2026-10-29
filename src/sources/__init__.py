"""数据源注册表。"""

from .juejin import JuejinSource
from .mianshiya import MianshiyaSource
from .nowcoder import NowcoderSource
from .prachub import PrachubSource

SOURCES = {
    JuejinSource.key: JuejinSource,
    MianshiyaSource.key: MianshiyaSource,
    NowcoderSource.key: NowcoderSource,
    PrachubSource.key: PrachubSource,
}

SOURCE_NAMES = {
    "nowcoder": "牛客网",
    "mianshiya": "面试鸭",
    "prachub": "PracHub",
    "juejin": "掘金",
}
