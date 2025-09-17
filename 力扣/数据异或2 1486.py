# 1486. 数组异或操作
# 简单
# 相关标签
# premium lock icon
# 相关企业
# 提示
# 给你两个整数，n 和 start 。

# 数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。

# 请返回 nums 中所有元素按位异或（XOR）后得到的结果。

 

# 示例 1：

# 输入：n = 5, start = 0
# 输出：8
# 解释：数组 nums 为 [0, 2, 4, 6, 8]，其中 (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8 。
#      "^" 为按位异或 XOR 运算符。
# 示例 2：

# 输入：n = 4, start = 3
# 输出：8
# 解释：数组 nums 为 [3, 5, 7, 9]，其中 (3 ^ 5 ^ 7 ^ 9) = 8.
# 示例 3：

# 输入：n = 1, start = 7
# 输出：7
# 示例 4：

# 输入：n = 10, start = 5
# 输出：2
 

# 提示：

# 1 <= n <= 1000
# 0 <= start <= 1000
# n == nums.length

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # 1. 定义一个列表 nums，用来存放生成的元素
        nums = []
        # 2. 循环 n 次，从 i=0 到 i=n-1
        for i in range(n):
            # 按照公式 nums[i] = start + 2*i 计算出元素，并添加到列表末尾
            nums.append(start + 2*i)
        
        # 3. 计算所有元素的异或结果
        result = 0 # 任何数和 0 异或都等于它本身，所以从 0 开始
        for num in nums:
            result = result ^ num # 使用 ^ 运算符进行按位异或
        return result