# res范围[0到10^7] 最高1人分上界的candies[i]  -> [0,max(a)]

#语言整理：给定长度为n的一组数a,和k个人，这组数任意拆分的小子堆，每个人一堆，求可以拿走的最大值res

# 思路：1.显然答案有界，界于区间[0,max(a)]
# 2.对res上界，即check表示恰好sum(x//res for x in a)<k sum(x // res for x in a) 就是我们计算“总共能分出多少份”的过程。


# 3.二分得到的结果-1是答案

class Solution:
    def maximumCandies(self,a:List[int],k:int) ->int:
        if sum(a) <k :return 0 
        lo,hi = 1,10**12+10
        def check(res):
            return sum(x//res for x in a)<k
        #x都代表数组a中的某一个元素 res for x in a 
        # res只是一个传参代号
        # for x in a 这个循环结构，正是为 x 提供了上下文，明确地告诉计算机 x 的值在每次迭代中是什么。
        while lo<hi:
            i=(lo+hi)>>1
            if check(i):
                hi=i
            else:
                lo=i+1
        return lo-1