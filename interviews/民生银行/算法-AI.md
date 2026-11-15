# 民生银行 · 算法/AI

> 共 **2** 条 ｜ [返回总目录](../../README.md)

---

## 中国民生银行信用卡中心金融科技挑战赛数据算法赛道面经

来源：牛客网 ｜ 类型：面经 ｜ 发布：2023-03-21 ｜ [原文链接](https://www.nowcoder.com/discuss/467827912239013888)

TimeLine ：线上初赛202208??，线下复赛20220822-20220826 

 当时的BG ：北邮本硕，管理类专业，两段实习经历：字节数据分析师、美团商业分析师 

 写在前面的话 ：以下问题的答案 必然 存在错误，敬请读者批评指正 

 

 线上初赛 

 主要考察算法和SQL，算法的难度不是特别高，但SQL有一定难度 

 民生银行卡中心的代码平台仅有上传功能，并不是OJ，因此只能在本地进行样例测试 

 初试没有屏幕监控，因此理论上可求助于任何渠道（划掉） 

 算法题 

 1. 

 题目描述： 

 

 输入格式：

 

 输出格式：

 

 
input_nums = []
while True:
 inputing = int(input())
 if inputing == -1:
 break
 else:
 input_nums.append(inputing)

res = [0] * len(input_nums)

for index in range(len(input_nums)):
 for i in range(1, input_nums[index] + 1):
 res[index] += input_nums[index]//i * i
 
for num in res:
 print(num)
 
input_nums = []
while True:
 inputing = int(input())
 if inputing == -1:
 break
 else:
 input_nums.append(inputing)

res = [0] * len(input_nums)

for index in range(len(input_nums)):
 for i in range(1, input_nums[index] + 1):
 tmp = []
 for j in range(1, int(i ** 0.5) + 1):
 if i % j == 0:
 tmp.append(j)
 tmp.append(int(i/j))
 res[index] += sum(set(tmp))
 
for num in res:
 print(num)
 2. 

 题目描述：

 

 输入格式：

 

 输出格式：

 

 
def isprime(x):
 if x = 4
order by client_id asc
 2. 

 数据表详情如下：

 

 数据表示例性字段如下：

 

 问题1：请用sql语句计算首次交易后第二天再次交易的用户的比率，四舍五入到小数点后两位 

 

 
with a as
(
 select client_id, trans_day,
 row_number() over(partition by client_id order by trans_day asc) as rn,
 date_sub(trans_day, interval rn day) as sub
 from trans_data
 where rn in (1, 2)
)
select round(count(client_id) / (select count(client_id) from trans_data group by client_id), 2) as Ratio
from a
group by client_id
having count(distinct sub) = 1
 问题2：请用sql语句查询每个客户最近一次交易的amount，将amount按降序排列并给出前20行 

 

 
with a as
(
 select client_id,
 trans_day, amount,
 row_number() over(partition by client_id order by trans_day desc) as rn
 from trans_data
)
select client_id, trans_day as '最近交易日期', amount
from a
where rn = 1
order by amount desc
limit 20
 线下复赛

 共有40名同学进入线下复赛环节，其中研发赛道20名，数据算法赛道20名

 每5人为1个小组，因此数据算法赛道共有4支队伍，每两支队伍共享一个复赛题目，题目内容与银行风控有关

 每支队伍需要在给定时间内，根据复赛的试题材料，进行线上打榜比赛，并制作PPT回答材料相关问题

 复赛时间为5天，较招行夏令营而言相对不那么累，奖励较为丰厚，有一半的队伍可获得数目不菲的奖金，因此相当推荐大家参与

---

## 春招结束

来源：牛客网 ｜ 类型：面经 ｜ 发布：2022-03-12 ｜ [原文链接](https://www.nowcoder.com/discuss/353159319749337088)

格力电器，广东珠海，软件开发，有餐补，无加班，双休，适合养老 

 
 

 北汽福田，北京，软件开发方面，不算特别高吧，国企都这样，但听说有北京户口 

 
 

 中芯国际，在上海，自动化算法工程师，包吃住，薪资中规中矩，大厂还是有保障 

 
 

 中讯邮电设计，郑州，老国企，吃住方面不是很清楚，国企永远不知道自己下个月会拿多少，说的是能力好的有多的 

 
 

 更新—————————————————————

 
 

 中石化四建，软件开发，跟着项目走经常出差，薪资没有互联网那么高，也是国企，和中讯邮电设计差不多

 
 

 还有，在这diss一下格力，录用编号下来了和签约说明会都参加了，最后给我发邮件说不符合岗位要求，反正也没想去格力

 
 

 
 

 更新—————————————————————

 
 

 上海移动笔试完，不知道有没有结果（估计没结果）

 已收到offer，不打算去薪资太低

 
 

 南京银行笔试一面已结束（没收到二面通知已凉）

 
 

 中国民生银行已笔试完等结果（题量巨大），无后续消息，已凉

 
 

 上海电器科学研究所两轮面试已结束，等谈资，等了一个月了估计没戏不去了

 
 

 中金所唐银公司一面结束（二面必须线下面，得去上海，等疫情结束，目前不考虑了）更新：一面通过，听说二面会报销来回车费和住宿，二面看情况

 
 

 永恒力叉车，德企，一面二面结束，在等终面（估计等不到，要等上海疫情结束再面）（已缩招不去了）

 
 

 建行科技岗笔试完，还没笔试就已经发终面通知，等终面，建设银行更新：等待一个小时，面试过程3分钟，感觉凉凉

 更新：进入到差额体检

 
 

 上海百秋电商运维开发，给的p2级但薪资一般，感觉除去各种基本开销一个月到手没多少，不打算去了

 
 

 综合考虑去中芯国际稳一些能学到东西，至此春招暂时结束

 
 

 欢迎各位大佬来讨论交流

---
