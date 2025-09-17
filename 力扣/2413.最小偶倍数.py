# 2413. 最小偶倍数
# 尝试过
# 简单
# 相关标签
# premium lock icon
# 相关企业
# 提示
# 给你一个正整数 n ，返回 2 和 n 的最小公倍数（正整数）。
 

# 示例 1：

# 输入：n = 5
# 输出：10
# 解释：5 和 2 的最小公倍数是 10 。
# 示例 2：

# 输入：n = 6
# 输出：6
# 解释：6 和 2 的最小公倍数是 6 。注意数字会是它自身的倍数。

class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n%2==0 : #=是赋值 ，==是判断
            return n
        else:
            return int(n*2)