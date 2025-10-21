from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        #考虑特殊情况
        #1.k=0，半径是0的时候每个avg[i]就是它自己
        avgs=[-1]*n
        if k==0:
            return nums
        window=2*k+1
        #2.窗口过大，直接运行不了
        if window >n:
            avgs=[-1]*n
            return avgs
        
        #这里的nums区间考虑：左闭右开，总长为2k+1,0为下标起点，那么右开端点为2k+1
        temp=sum(nums[0:2*k+1])
        avgs[k]=temp//window
        for i in range(k+1,n-k):
            #开始滑动窗口 改变sum值，从而改变avgs值，该当i从k变成k+1时，本该移除的i-k变远了1位，所以是i-k-1，右边进入i+k
            temp -= nums[i-k-1]
            temp += nums[i+k]    
            avgs[i]=temp //window
        return avgs

    