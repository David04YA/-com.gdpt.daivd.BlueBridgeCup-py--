# 584. 寻找用户推荐人
# 已解答
# 简单
# 相关标签
# premium lock icon
# 相关企业
# 提示
# SQL Schema
# Pandas Schema
# 表: Customer

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | referee_id  | int     |
# +-------------+---------+
# 在 SQL 中，id 是该表的主键列。
# 该表的每一行表示一个客户的 id、姓名以及推荐他们的客户的 id。
# 找出以下客户的姓名：

# 被任何 id != 2 的用户推荐。
# 没有被 任何用户推荐。
# 以 任意顺序 返回结果表。

# 结果格式如下所示。

 

# 示例 1：

# 输入： 
# Customer 表:
# +----+------+------------+
# | id | name | referee_id |
# +----+------+------------+
# | 1  | Will | null       |
# | 2  | Jane | null       |
# | 3  | Alex | 2          |
# | 4  | Bill | null       |
# | 5  | Zack | 1          |
# | 6  | Mark | 2          |
# +----+------+------------+
# 输出：
# +------+
# | name |
# +------+
# | Will |
# | Jane |
# | Bill |
# | Zack |
# +------+


# Write your MySQL query statement below

select name from Customer where ifnull(referee_id,0)<>2