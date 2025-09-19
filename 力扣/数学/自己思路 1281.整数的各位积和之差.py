# 1281. 整数的各位积和之差
# 简单
# 相关标签
# premium lock icon
# 相关企业
# 提示
# 给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。

 

# 示例 1：

# 输入：n = 234
# 输出：15 
# 解释：
# 各位数之积 = 2 * 3 * 4 = 24 
# 各位数之和 = 2 + 3 + 4 = 9 
# 结果 = 24 - 9 = 15
# 示例 2：

# 输入：n = 4421
# 输出：21
# 解释： 
# 各位数之积 = 4 * 4 * 2 * 1 = 32 
# 各位数之和 = 4 + 4 + 2 + 1 = 11 
# 结果 = 32 - 11 = 21
 

# 提示：

# 1 <= n <= 10^5

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        #思路：不断循环，直到n变成个位数的时候，循环结束，得出相加值，相乘值
        sump = 0
        sumx = 1
        temp=n
        
        while temp > 0:
         temp2 = temp%10
         sumx *= temp2
         sump += temp2
         temp //= 10
        return sumx-sump


#  超出时间限制
