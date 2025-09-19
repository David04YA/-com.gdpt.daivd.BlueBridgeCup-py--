# 258. 各位相加
# 简单
# 相关标签
# premium lock icon
# 相关企业
# 提示
# 给定一个非负整数 ，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。num

 

# 示例 1:

# 输入: num = 38
# 输出: 2 
# 解释: 各位相加的过程为：
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# 由于 2 是一位数，所以返回 2。
# 示例 2:

# 输入: num = 0
# 输出: 0
 

# 提示：

# 0 <= num <= 231 - 1
 

# 进阶：你可以不使用循环或者递归，在 时间复杂度内解决这个问题吗？O(1)
import typing
from typing import List
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:  # 循环，直到 num 变为一位数
            sum_digits = 0  # 初始化各位之和
            temp = num # 临时变量，用于计算各位之和
            while temp > 0:
                sum_digits += temp % 10  # 取个位数加到 sum
                temp //= 10             # 移除个位数
            num = sum_digits  # 更新 num 为各位之和
        return num  # 返回最终的一位数结果
    
    # 实现目的：循环，直到num变成一位数，这里的num变化通过临时变量temp代替
