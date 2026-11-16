# 民生银行 · 算法/AI

> 共 **1** 条 ｜ [返回总目录](../../README.md)

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
