from collections import defaultdict

from typing import List
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        #考虑特殊情况.这样的子数组根本不存在，k==0 k>len m>k m>len m=0，以上情况全都被题设做好，我们不用考虑
        n=len(nums)
        #怎么做？1.先判断这个子数组真的有至少m个不同元素吗？->2.如果这个子数组真的有m个不同元素，把他们的和返回
        #m<=k<=len(nums)，可以这样考虑：用键值对的方式存储窗口内元素重复的数量，如果在哈希表key-value形式中，key的值都>=m,那么肯定满足了至少m个不同元素的题设。->为什么？因为 从取极端方法来看，key最多有k个，最少有1个。那么就存在一个数值从m到k,满足题设>=m。在本题上,这个哈希表既承担了记录元素的功能，又承担了记录相同元素有多少个的功能
        counts=defaultdict(int)
        #形成第一个窗口时，存储数据
        temp_sum=final_sum=0
        for i,j in enumerate(nums[0:k]):
            counts[nums[i]]+=1
            temp_sum +=j
        #做判断，如果没有满足m个不相同元素的条件，根本就不把临时变量存储
        if len(counts)>=m:
            final_sum=max(temp_sum,final_sum)
        #在第二个窗口开始滑动
        # for i,j in enumerate(nums[k:]):
            
                    
                    #enumerate()和range()的不同：enumerate()是切片操作，从0开始，range(start,end)从start开始，end结束
                

        for i in range(k,n):
#先移除上一个窗口的左端点 [L,R] K 的左端点为R-L+1=K,L=R-K+1 那么在R进1的情况下，想减去前一个窗口的左端点就变成R-K+1-1=R-K
            counts[nums[i-k]] -= 1
            counts[nums[i]] +=1
            temp_sum += nums[i]
            # temp_sum += j
            temp_sum -= nums[i-k]
            if len(counts)>=m:
                final_sum=max(temp_sum,final_sum)
        return final_sum
    
    # 当一个数字在窗口内的计数变为 0 时，你没有将它从字典 counts 中删除。
