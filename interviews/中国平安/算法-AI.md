# 中国平安 · 算法/AI

> 共 **6** 条 ｜ [返回总目录](../../README.md)

---

## 中国平安 Agent应用开发(实习) 一面

来源：牛客网 ｜ 类型：面经 ｜ 发布：2026-09-10 ｜ [原文链接](https://www.nowcoder.com/discuss/927643502077317120)

1. 请做一下自我介绍 

 2. 你设计的Agent 怎么划分模块的 

 3. RAG 系统中，如何处理多语言文档和跨语言检索 

 文档入库时保留原文、语言、国家、渠道、版本和生效时间。切分不能只按照固定字符数，还需要识别标题、条款、表格和 FAQ 的语义边界。 

 查询阶段可以采用两路召回： 

 原语言向量召回
 +
统一语义空间向量召回
 +
关键词检索
 -> 融合排序
 
 对于中文问题查询英文政策，先抽取业务实体和限定条件，再生成跨语言查询向量。排序时增加国家、渠道、商品类型和政策生效时间的过滤，避免语义相似但适用范围错误的文档被召回。 

 最终上下文必须携带来源语言和原文片段。生成结果涉及金额、时效和资格条件时，优先引用原始条款，不应仅根据翻译后的摘要回答。 

 4. PDF 中同时存在正文、表格和扫描图片时，如何建立解析流程 

 先判断 PDF 是文本型还是扫描型。文本型文件直接提取字符、字体坐标和版面结构；扫描型文件先转图片，再进行 OCR。表格不能简单按换行拼接，需要根据坐标聚类恢复行列关系。 

 PDF 类型识别
 -> 文本层提取
 -> 页面布局分析
 -> 表格检测
 -> 图片区域 OCR
 -> 页眉页脚清洗
 -> 章节与条款重建
 -> 结构化切分
 -> 质量抽检
 
 表格内容建议同时保存 Markdown 和结构化 JSON 两份结果。对于低置信度 OCR，应记录页码、坐标和置信度，进入人工校验队列。解析后的内容还要和原 PDF 页码建立映射，便于回答时返回可定位引用。 

 5. 知识库如何处理政策版本更新和历史有效期 

 知识库不能只保存一份最新文本。每个文档需要有版本号、生效时间、失效时间、适用国家、业务渠道和来源地址。 

 检索时将用户问题中的业务时间作为过滤条件： 

 SELECT chunk_id, content, version
FROM policy_chunk
WHERE country = ?
 AND effective_at ?);
 
 如果用户没有明确时间，可以默认使用当前有效版本，但回答中要避免暗示历史政策同样适用。更新流程应先完成新版本解析、质量检查和离线评测，再切换索引别名。切换失败时保留旧索引，不能出现索引已经切换但元数据仍指向旧版本的状态。 

 6. 如何判断一次 RAG 回答到底错在召回还是生成 

 需要把链路拆成独立评测阶段。召回阶段看目标证据是否进入候选集合，生成阶段看模型是否正确使用了已召回证据。 

 可以记录： 

 
 Recall@K 

 证据覆盖率 

 证据排序位置 

 引用准确率 

 结论与证据的蕴含关系 

 无证据回答比例 

 
 如果正确条款没有出现在前 K 个结果中，问题主要在查询改写、切分、索引或排序；如果正确条款已经召回，但模型仍然编造或误读，则问题在上下文组织、模型能力或生成约束。 

 高风险场景可以要求模型输出结构化结论： 

 {
 "decision": "需要人工审核",
 "evidence": [
 {
 "document_id": "policy-2026-03",
 "page": 12,
 "quote": "..."
 }
 ],
 "missing_conditions": ["商品签收时间"]
}
 
 7. 如何给 Agent 工具设计幂等和重试机制 

 每次工具调用生成稳定的操作 ID，并将工具名称、用户 ID、业务参数摘要和任务 ID 纳入幂等键。工具服务需要记录执行状态： 

 INIT -> RUNNING -> SUCCEEDED
 -> FAILED
 -> UNKNOWN
 
 UNKNOWN 表示请求超时，但无法确认对端是否已经成功，不能直接重试副作用操作。应先通过查询接口确认结果。 

 def execute_once(operation_id, action):
 record = store.get(operation_id)

 if record and record.status == "SUCCEEDED":
 return record.result

 if record and record.status == "UNKNOWN":
 return reconcile(operation_id)

 store.create_if_absent(operation_id, status="RUNNING")

 try:
 result = action(operation_id)
 store.mark_success(operation_id, result)
 return result
 except TimeoutError:
 store.mark_unknown(operation_id)
 raise
 
 对于查询类工具可以有限重试；对于退款、取消和改址类工具，必须先确认幂等能力和最终状态。 

 8. 大模型输出 JSON 经常不完整，如何提高解析成功率 

 不能只依赖 prompt 要求模型输出 JSON。服务端应该使用结构化输出或 JSON Schema 约束，并设置最大字段长度、枚举值和必填字段。 

 解析失败时先尝试从响应中提取代码块或首尾 JSON，但不能用宽松正则替代真正的 JSON 解析。修复请求只发送解析错误和 Schema，不把整段历史再次重复拼接。 

 from pydantic import BaseModel, Field, ValidationError

class Action(BaseModel):
 name: str
 arguments: dict
 confidence: float = Field(ge=0, le=1)

def parse_action(text: str) -> Action:
 try:
 return Action.model_validate_json(text)
 except ValidationError as exc:
 raise ValueError(f"invalid structured output: {exc}") from exc
 
 如果多次修复仍失败，应切换到人工处理或固定模板，而不是无限调用模型。 

 9. Agent 如何实现权限控制，防止模型越权 

 权限判断必须在工具服务端完成，不能只写在系统提示词里。每个工具声明资源范围、操作类型、风险等级和所需权限。 

 读取订单信息：用户本人订单
修改收货地址：订单未发货且用户二次确认
退款：满足退款条件且需要支付权限
导出数据：禁止模型直接调用
 
 模型请求中携带的用户 ID、租户 ID 和权限上下文应由服务端注入，不能信任

---

## 8.11秋招正式批投递记录

来源：牛客网 ｜ 类型：面经 ｜ 发布：2026-08-12 ｜ [原文链接](https://www.nowcoder.com/feed/main/detail/1a98e2c33d57400d8dc92d032df3508d)

个人背景看主页其他帖子，普通本科，软科 30‑50 区间。目前正在 3C 企业做第四段实习，做过 Agent 相关以及传统 React 项目，没有海外经历，算是很典型的普通应届生情况。
投递主要瞄准大模型前端、策略产品，意向行业覆盖新能源、消费电子、光伏储能、新消费、游戏以及中小互联网厂。

流程推进中：
卓驭｜测评结束，业务评估后淘汰
远景｜完成测评，正在评估
Babycare｜测评做完，电话面结束，等待业务回复
JDS｜完成测评 + AI 面试
蔚来｜测评→提前批一面→二面结束
小米｜已参与海测
Vivo｜一面结束，大概率凉凉
新华三｜完成海测
中国平安｜测评完成，等待一面
Shopee｜一面结束
作业帮｜一面结束
搜狐畅游｜一面结束
宇树科技｜一面结束（转正实习岗）

已经收到淘汰：
科大讯飞、百度管培、字节生服第一志愿、Garena、Sharpa、岚图汽车、4399、Magic Taevin
还有不少没收到拒信的，估计已经默拒，就懒得挨个去官网核对了

面试一波接一波，有挂有继续推进，基础坚持一定会胜利！ #秋招投递记录#

---

## 中国平安春招二面

来源：牛客网 ｜ 类型：面经 ｜ 发布：2026-04-07 ｜ [原文链接](https://www.nowcoder.com/feed/main/detail/4b0bc7cb57d941ffa05a46cb36873fe7)

#春招# 
4.7
时间：40min
1.自我介绍
2.六级，英语现在水平
3.实习怎么是测开？
4.项目的背景，团队成员，你负责什么
5.项目是否从0到1，较为复杂的功能是什么？
6.视频续播怎么优化？
7.分布式锁是否能够防止超发，如果两个线程就是同时抢，能锁的住吗？
8.探讨优惠券超发的场景，结合12306等等
9.项目中的AI功能是什么模型，版本是多少？
10.实习过程中怎么调用大模型的，要翻墙吗？
11.平时还会什么语言
12.在这个专业你的特长是什么？
13.AI工具的使用频率，怎么用的？
14.研究生最有价值的事

---

## 平安科技| 算法部门直招，其余也可内推，速度给反馈

来源：牛客网 ｜ 类型：面经 ｜ 发布：2021-06-22 ｜ [原文链接](https://www.nowcoder.com/discuss/353158031292702720)

我们是 平安科技 旗下 金融壹账通 的加马平台，三个岗位可部门直招，分别是nlp团队，cv团队和ai工程化团队，发送简历到CHENJIAHAO637@pingan.com.cn 即可，会速度反馈，安排面试，面试进度的事情私聊我就行。校招生也ok，我们没那么看中工作经验(仅限于其中的nlp岗位，其他是别人招聘的，我不知道)。

 PS:目前如果是校招，直接去平安招聘官网，我的内推码是PADKbOE3，目前直接我决定的名额都是社招了。

 

 工作地点在上海或深圳，上班时间965，绝对没有加班。

 此外如果对平安旗下其余岗位感兴趣

 可参考 中国平安招聘 ，简历也可以发我邮箱，我帮内推😁。

 

 简历名备注姓名➕岗位

 

 直接给链接吧https://wetalent.pingan.com/3e4515cd64c838ad990afdbe48f9cda2/search

 

 招聘要求

---

## 一年经验总结贴

来源：牛客网 ｜ 类型：面经 ｜ 发布：2021-06-05 ｜ [原文链接](https://www.nowcoder.com/discuss/353157997318840320)

考公

 
 
 
 行测看完，申论 
 

 

 
 ***佛山市高明区委组织部

佛山高新技术产业开发区南海园管理局

***深圳市南山区委组织部

 
 国考

 
 广东选调生，浙江选调

 
 

 
 公司招聘

 
 

cyc 2018和java guide

工作攻略： https://1o24bbs.com/t/topic/8336 

 
 
 
 

 

 
 11月4日下午1点半 平安普惠 算法 
 

 
 10月29日 的南方电网 
 

 
 10月29日14:00-22:00 三七互娱65分钟笔试 
 

 
 10月24 日 19点 上交所技术 
 

 
 中信银行 实际考试 10月26日14：00到16：00 
 

 
 10月26日招商银行 笔试9点半到12点 
 

 
 10月24日 14点到15点 推荐算法一面 TCL 
 

 
 10月22 联易融 16：00-24：00 
 

 
 10 21号奇安信 算法岗 
 

 
 10月21日 海康威视 大数据 
 

 
 10月21日 拼多多 算法 
 

 
 10月20号上午 9点40-10点招商银行 信息科技岗 
 

 
 10月20号上午 11点10-11点20 安信证券 开发 算法 
 

 
 10月18 14：00到16：00 招商银行 
 

 
 10月17号 中国人寿 20点 
 

 
 10月17号富途一面 
 

 
 10月17号 招联金融 
 

 
 10月17中信银行 
 

 
 10月17号 10点 到12点招商金科 
 

 
 中信银行 信息科技已经应聘 
 

 
 10月5号已投递IBM 开发岗位 
 

 
 招商证券 金融科技 
 

 
 南方基金 
 

 
 三七互娱 机器学习开发工程师 
 

 
 10号14：00 富途 C后台 
 

 
 11号 10点 字节跳动 客户端 
 

 
 10月14号 工商银行 
 

 
 10月15号 中国移动 14：00-16：00 
 

 
 工商银行 9 26日 
 

 
 9月26农业银行 早上 9点到11点55 
 

 
 9月26迈瑞医疗 晚上19点 
 

 
 安信证券 9-23开发 算法 
 

 
 商汤科技 
 

 
 晚上9月18号，7点到8点 
 

 
 平安科技 8点到9点30 
 

 
 平安产险 
 

 
 21号 晚上 腾讯微保 
 

 
 字节 9月20日笔试 
 

 
 网易 8月23日 深度学习算法工程师 
 

 
 招银网络：9月6日 14：00-16：00 
 

 
 字节跳动：9月6日 10：00 
 

 
 腾讯微保 视觉+后台 
 

 
 中国移动 8月21日 AI 开发 
 

 
 9月17 云从科技 C++开发 
 

 
 9月17 欢聚时代 C++开发 
 

 
 虎牙 9月17 C++ 后台 
 

 
 Bigo C++ 9月17日 
 

 
 快手 8月24 计算机视觉&& C++ 
 

 
 招商银行卡中心 8月27日 研发岗 
 

 
 依图科技 9月3日 算法 
 

 
 迈瑞 9月4日 医疗图像处理 
 

 
 顺丰 机器学习工程师 9月4号 
 

 
 越秀金控 
 

 
 vivo 算法岗位 
 

 
 oppo 算法岗位 
 

 
 平安产险总部 8月30日 产品 or 算法 
 

 
 深信服 算法+开发 9月7号 
 

 
 招商银行 9月7号 
 

 
 鹏华基金：助理量化研究员 9月7日 
 

 
 微众银行 9月7号 风险算法 和策略分析岗位 
 

 
 TP-Link 算法已投递 
 

 
 CVTE 
 

 
 招联金融9月17号软件开发

---

## 每日社招岗位推荐3.24（适合0-3年）

来源：牛客网 ｜ 类型：面经 ｜ 发布：2021-03-24 ｜ [原文链接](https://www.nowcoder.com/discuss/353157705638551552)

每日站内社招消息汇总

 
 ------------------------

 
 
 平安科技-资深开发工程师

 https://www.nowcoder.com/fulltime/42343?jobIds=50780&ncsr= 

深信服-大数据开发工程师

 https://www.nowcoder.com/fulltime/48066?jobIds=44522&ncsr= 

启林投资-量化开发工程师

 https://www.nowcoder.com/job/42921?jobIds=39206 

涂鸦智能-高级Java开发工程师-OS业务平台

 https://www.nowcoder.com/fulltime/48505?jobIds=45990&ncsr= 

深信服-软件测试工程师

 https://www.nowcoder.com/fulltime/48066?jobIds=44523&ncsr= 

渤海银行-Java 开发工程师

 https://www.nowcoder.com/fulltime/25753?jobIds=39517&ncsr= 

深圳蓝贝科技有限公司-Android工程师

 https://www.nowcoder.com/fulltime/37766?jobIds=42332&ncsr= 

用友-高级Java开发工程师

 https://www.nowcoder.com/fulltime/53413?jobIds=50702&ncsr= 

百度-后端系统开发工程师Python方向

 https://www.nowcoder.com/fulltime/52412?jobIds=49665&ncsr= 

陌陌-H5前端开发工程师

 https://www.nowcoder.com/fulltime/32294?jobIds=37197&ncsr= 

美团团好货-高级java工程师
 

 
 https://www.nowcoder.com/fulltime/52899?jobIds=50256&ncsr= 
 

 
 百融云创科技股份有限公司-数据分析师

 https://www.nowcoder.com/fulltime/48509?jobIds=46932&ncsr= 

帆软软件-数据分析师

 https://www.nowcoder.com/fulltime/25602?jobIds=38745&ncsr= 

中智诚科技产业发展有限公司-高级数据产品开发工程师

 https://www.nowcoder.com/fulltime/47472?jobIds=43489&ncsr= 

字节跳动-数据分析师【短视频】

 https://www.nowcoder.com/fulltime/29714?jobIds=50751&ncsr= 

深圳致星科技有限公司-产品经理/专家（安全方向）

 https://www.nowcoder.com/fulltime/28573?jobIds=40674&ncsr= 

北京所思信息科技有限责任公司-产品经理（北京/上海）

 https://www.nowcoder.com/fulltime/46032?jobIds=47992&ncsr= 

北京琥珀创想科技有限公司-产品经理（海外市场）

 https://www.nowcoder.com/fulltime/35432?jobIds=49328&ncsr= 

帆软软件-SEO运营

 https://www.nowcoder.com/fulltime/25602?jobIds=47999&ncsr= 

网易-海外游戏运营（日语）

 https://www.nowcoder.com/fulltime/47222?jobIds=50257&ncsr= 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 
 

 
 ------------------------
 

 
 

 
 点击链接私聊岗位发布者，与内推人直接沟通！

-更多社招职位： https://www.nowcoder.com/fulltime/center 

 
 

 
 
 欢迎关注【牛客职盐】，查看最新社招面经合集！
 

 
 
 

 
 
 

 
 欢迎加入牛客社招交流群，一起交流社招相关信息~每天还有社招岗位推荐哦~

---
