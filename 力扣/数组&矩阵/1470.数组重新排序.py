# 1470. 重新排列数组
# 已解答
# 简单
# 相关标签
# premium lock icon
# 相关企业
# 提示
# 给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

# 请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

 

# 示例 1：

# 输入：nums = [2,5,1,3,4,7], n = 3
# 输出：[2,3,5,4,1,7] 
# 解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]
# 示例 2：

# 输入：nums = [1,2,3,4,4,3,2,1], n = 4
# 输出：[1,4,2,3,3,2,4,1]
# 示例 3：

# 输入：nums = [1,1,2,2], n = 2
# 输出：[1,2,1,2]
 

# 提示：

# 1 <= n <= 500
# nums.length == 2n
# 1 <= nums[i] <= 10^3
import math
from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        #切片，要求分成几个数组就切几个
        #变量：1.x数组 2.y数组 3.用于返回值的数组
        #切片完如何添加？ append右进
        x_arr = []
        y_arr = []
        res_arr= []
        x_arr= nums[0:n:]
        y_arr= nums[n:]
        for i in range(n):
            res_arr.append(x_arr[i])
            res_arr.append(y_arr[i])
        return res_arr