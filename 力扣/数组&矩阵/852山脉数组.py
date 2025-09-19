# # 我的尝试:二分查找
# # class Solution:
# #     def peakIndexInMountainArray(self, arr: List[int]) -> int:
# #         left= 0 
# #         right = len(arr)
# #         mid = int(right/2)
# #         while(left<right):
# #             if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
# #                 break
# #             if arr[mid+1]>arr[mid]:
# #                left = mid
# #             elif arr[mid+1]<arr[mid]:
# #                 right=mid
# #         return mid

# mid 的计算位置：在二分查找中，mid 索引必须在 while 循环的每一次迭代中重新计算，这样才能不断缩小搜索范围。你的代码只在循环开始前计算了一次。
# 循环终止条件：if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]: break 这个判断本身是正确的，但更标准的二分查找模式是通过收缩 left 和 right 指针直到它们相遇来找到目标，这种方式更健壮。
# 无限循环风险：left = mid 和 right = mid 这两行代码可能会导致无限循环。例如，当 left = 3, right = 4 时，mid 会是 3。如果此时满足 arr[mid+1] > arr[mid]，left 会被再次赋值为 3，循环无法前进。标准的做法是使用 left = mid + 1 或 right = mid - 1 来确保区间总是在缩小。
# right 的边界：通常将 right 初始化为 len(arr) - 1 会更方便，这样 left 和 right 就始终是数组的有效索引，可以简化边界处理。