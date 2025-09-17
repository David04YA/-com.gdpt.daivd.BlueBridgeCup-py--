from typing import List
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        #先做好计数器来暴力算法
        count = 0
        n=len(arr)
        # for i in len(arr): len(arr)返回的是一个整数（数组的长度），而for in需要一个可以迭代的对象
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if abs(arr[i]-arr[j]) <= a and \
                       abs(arr[j]-arr[k]) <=b and \
                       abs(arr[i]-arr[k]) <=c:
                       count += 1
        return count