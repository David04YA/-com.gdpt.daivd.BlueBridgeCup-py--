# 若 n=2 
# x
#   且 x 为自然数（即 n 为 2 的幂），则一定满足以下条件：

# 恒有 n & (n - 1) == 0，这是因为：
# n 二进制最高位为 1，其余所有位为 0；
# n−1 二进制最高位为 0，其余所有位为 1；
# 一定满足 n > 0。
# 因此，通过 n > 0 且 n & (n - 1) == 0 即可判定是否满足 n=2 
# x
#  。

# 作者：Krahets
# 链接：https://leetcode.cn/problems/power-of-two/solutions/12689/power-of-two-er-jin-zhi-ji-jian-by-jyd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 位与操作:在二进制中,当两个位都是1时,结果才是1,否则是0

def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0