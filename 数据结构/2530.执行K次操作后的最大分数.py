#贪心策略，每次操作都选择数组中最大值，要求我们实现两个功能：
#1.快速找到并弹出当前集合中的最大值
#2.将一个新计算出的值插入回集合中
#这两个要求使我们使用大根堆 堆顶永远是最大元素，获取操作的时间复杂度是 O(1)。
# 删除最大值：heappop 操作的时间复杂度是 O(log n)。
# 插入新元素：heappush 操作的时间复杂度是 O(log n)。
from heapq import *
from math import *
class Solution:
    def maxKelements(self,nums:list[int],k:int)->int:
        res=0
        hq=[]
        for i,x in enumerate(nums):
            nums[i]=-x
            heappush(hq,-x) #由于是大根堆，采用取反思想
            #heappush(heap,item)堆，元素。插入元素并按照小根堆性质排序（从小到大)
        for _ in range(k):
            x=heappop(hq) #heappop总是弹出小根堆中的最小值
            res += x
            heappush(hq,-ceil(-x/3))
        return -res