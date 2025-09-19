from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # 初始化左右指针，进行二分查找
        # 我们使用数组的有效索引范围
        left, right = 0, len(arr) - 1

        # 循环继续的条件是搜索空间不止一个元素
        # 当 left == right 时，循环终止，我们找到了目标
        while left < right:
            # 计算中间索引
            mid = (left + right) // 2

            # 检查我们是否在上升坡
            if arr[mid] < arr[mid + 1]:
                # 如果在上升，峰顶一定在 mid 的右边
                # 所以我们舍弃左半部分，包括 mid
                left = mid + 1
            else:
                # 如果在下降（或在峰顶），峰顶就在 mid 或其左边
                # 所以我们舍弃右半部分。我们保留 mid，因为它可能就是峰顶
                right = mid
        
        # 当循环结束时，left 和 right 指针会汇合在峰顶的索引上
        return left
