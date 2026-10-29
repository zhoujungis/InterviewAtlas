# 深度求索 · 算法/AI

> 共 **3** 条 ｜ [返回总目录](../../README.md)

---

## DeepSeek（深度求索）——AI Agent 开发岗 社招一面

来源：牛客网 ｜ 类型：面经 ｜ 发布：2026-09-08 ｜ [原文链接](https://www.nowcoder.com/discuss/926970960375214080)

更像技术合伙人之间的设计讨论。"不考知识点，聊设计、聊趋势、聊想法"。全程 90 分钟，从项目架构到评测体系到 Loop Engineering。

 
 开场与项目讨论

 
 
 你最近在关注 Agent 领域的什么新技术？——你说你关注了 DeepSeek-Harness，你怎么理解它和 LangChain 的本质区别？Harness 解决了什么 LangChain 解决不了的问题？

 

 
 选一个你做得最满意的 Agent 项目，完整讲一遍。——从业务背景到技术方案到落地效果。不要报菜名（说用了 RAG、用了 Multi-Agent），我要听设计决策背后的思考。

 

 
 
 架构设计深度追问

 
 
 你的 Agent 整体架构是分几层的？——每一层的职责是什么？层与层之间的接口是怎么设计的？为什么这么设计？如果换一种分层方式会有什么不同？

 

 
 你的 Agent 是用的 ReAct 还是 Plan-and-Execute？——为什么选这个？如果任务更复杂（比如 50 步的长链路），你的方案还 work 吗？怎么改进？

 

 
 多 Agent 协作是怎么实现的？——通信模式是什么？如果子 Agent 返回的结果是自然语言（而不是结构化数据），主 Agent 怎么解析？怎么保证解析不出错？

 

 
 
 评测与 Badcase 回流

 
 
 你的 Agent 评测体系是怎么搭建的？——评测集覆盖了多少场景？怎么构造的？如果评测集里 30% 的 case 答案有主观性，你怎么处理？

 

 
 Badcase 怎么回流到训练/优化流程里？——你是不是直接把失败轨迹拿出来重新做 SFT？如果是，有什么问题？如果不是，你的完整处理链路是

---

## DeepSeek（深度求索）- Agent 开发 / Harness 方向

来源：牛客网 ｜ 类型：面经 ｜ 发布：2026-09-07 ｜ [原文链接](https://www.nowcoder.com/discuss/926274134261141504)

体验最佳！面试官像技术合伙人，全程“聊设计”。开场问“最近关注什么新技术”，我提 DeepSeek-Harness，他眼睛一亮，讨论了 20 分钟 Harness vs LangChain。场景题“多人协作 Agent 平台”他不断帮我补细节。第二天 HR 约二面。DeepSeek 招有想法的人。

 
 
 DeepSeek-Harness 与传统 LangChain 的核心区别？

 
 Agent Loop 的“早停”机制（已得可靠结论时提前终止）？

 
 工具调用沙箱（文件/网络/CPU 限制）设计？

 
 Spec-driven development 在 AI 时代与 Agent 的结合？

 
 Agent“长期规划能力”的 benchmark 设计？

---

## DeepSeek（深度求索）- Agent 开发 / Harness 方向（独角兽）

来源：牛客网 ｜ 类型：面经 ｜ 发布：2026-09-04 ｜ [原文链接](https://www.nowcoder.com/discuss/925527442863714304)

这是我面试体验最好的一场！面试官像个技术合伙人，全程在跟我“聊设计”而不是“考知识点”。开场没有让我自我介绍，而是直接问“你最近在关注 Agent 领域的什么新技术？”我提了 DeepSeek-Harness，他眼睛一亮，于是我们花了 20 分钟讨论 Harness 和 LangChain 的本质区别。后面他出了一个场景题“设计一个多人协作的 Agent 平台”，我说了思路，他不断帮我补充细节，像在开技术讨论会。虽然题目很难，但面完我很兴奋。最后他夸我技术视野不错，第二天 HR 就约了二面。DeepSeek 真的在招有想法的人，而不是背八股的人。

 
 
 你如何理解 DeepSeek-Harness？它与传统 LangChain 的核心区别是什么？

 
 在设计 Agent Loop 时，如何实现“早停”机制？模型已得可靠结论时如何提前终止？

 
 如何设计工具调用沙箱？如何限制文件系统、网络和 CPU 资源？

 
 “Spec-driven development”在 AI 时代如何与 Agent 结合？

 
 如何评估 Agent 的“长期规划能

---
