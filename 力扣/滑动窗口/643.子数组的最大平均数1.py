
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #传入参数：n k k为规定的区间长度 n为数组内元素个数
        #定义临时存储和用于返回的存储变量
        temp=0
        
        xum=float('-inf')
        for i,j in enumerate(nums):
            temp +=j
            left = i-k+1
            if left>=0:
             xum=max(temp,xum)
             temp -= nums[i-k+1]
            
        return xum/k
    
#     使用滑动窗口思路求解。
# 滑动窗口通用元素：
# 1.存储临时总和和存储真正总和的变量，用max或min等方法做一个判断，具体哪个方法依照题目规定使用
# 2.定义好左端点，左端点能做滑动窗口题中大部分需求：例1.判断是否开始滑动
# 例2.判断什么时候弹出左端点结束本次滑动
# 需要注意左端点的弹出

# 作者：绝望之谷
# 链接：https://leetcode.cn/problems/maximum-average-subarray-i/solutions/3792754/du-li-si-kao-de-chu-by-jue-wang-zhi-gu-n-c1kp/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。