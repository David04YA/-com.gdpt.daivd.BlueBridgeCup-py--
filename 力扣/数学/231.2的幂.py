class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 1. 2的幂次方首先必须是正数。
        if n <= 0:
            return False

        # 2. 循环地将 n 除以 2，只要它还能被 2 整除。
        #    一个数如果是2的幂，那么它一定不包含奇数因子（除了1）。
        while n % 2 == 0:
            n //= 2

        # 3. 循环结束后，如果 n 最终变成了 1，
        #    说明它最初只包含因子 2，因此是 2 的幂。
        return n == 1
    
    # class Solution:
    # def isPowerOfTwo(self, n: int) -> bool:
    #     #思路：能被2取余为0的数，是2的倍数，不一定是2的幂次方。
    #     # 2的幂次方--不断÷2后最后变成1
    #     if n%2==0:
    #         while n>=2:
    #             n//=2
    #     if n == 1:
    #      return True
    # 因为是一个向下取整，所以当执行while n>=2时 3会执行 3//=2 = 1，这种写法不行
  