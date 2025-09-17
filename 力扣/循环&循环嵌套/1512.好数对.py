# 1512. 好数对的数目
# 简单
# 相关标签
# premium lock icon
# 相关企业
# 提示
# 给你一个整数数组 nums 。

# 如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。

# 返回好数对的数目。

 

# 示例 1：

# 输入：nums = [1,2,3,1,1,3]
# 输出：4
# 解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始
# 示例 2：

# 输入：nums = [1,1,1,1]
# 输出：6
# 解释：数组中的每组数字都是好数对
# 示例 3：

# 输入：nums = [1,2,3]
# 输出：0
 

# 提示：

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
import typing
from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # 1. 定义一个计数器，初始为 0，用来记录好数对的数量
        count = 0
        # 2. 获取数组的长度，方便后面使用
        n = len(nums)
        
        # 3. 使用双重循环来生成所有可能的数对 (i, j)
        # 外层循环遍历 i，从 0 到 n-2
        for i in range(n):
            # 内层循环遍历 j，从 i+1 到 n-1，这样可以保证 i < j
            for j in range(i + 1, n):
                # 4. 判断是否是好数对
                if nums[i] == nums[j]:
                    # 如果是，计数器加 1
                    count += 1
        # 5. 所有循环结束后，返回最终的计数结果

        # range(n)左闭右开
        return count
