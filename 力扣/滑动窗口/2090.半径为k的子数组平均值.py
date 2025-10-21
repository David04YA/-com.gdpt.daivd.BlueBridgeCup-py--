

# 索引错误 (IndexError)：你初始化了一个空列表 avg=[]，但随后尝试通过索引 avg[i] = -1 来赋值。这会立即导致程序崩溃，因为你不能给一个不存在的索引位置赋值。
# 效率问题 (Time Limit Exceeded)：在 for i 循环内部，你又用了一个 for y 循环来计算子数组的和。这种嵌套循环的方法时间复杂度是 O(n * k)，当 n 和 k 很大时，会导致超时。
# 逻辑错误：temp -= nums[left] 这行代码看起来像是滑动窗口的尝试，但它的位置和 temp 的重置逻辑不正确，无法正确地更新窗口和。
# 真正的滑动窗口，是在上一个窗口和的基础上，通过“加一个、减一个”来直接得到当前窗口的和，完全不需要内层循环。


# 原始想法：以中心点 c 为基准进行思考。窗口是 [c-k, c+k]。这是一个非常直观和自然的想法。
# 代码实现：以窗口的右边界 i 为基准进行迭代。窗口是 [i-2k, i]，其中心点是 i-k。

from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        # 1. 初始化结果数组，默认所有元素的平均值都为 -1
        #    这完美解决了原代码中对空列表使用索引赋值 (avg[i]=...) 导致的 IndexError
        averages = [-1] * n

        # 如果 k 为 0，每个元素的平均值就是它本身
        if k == 0:
            return nums

        # 2. 定义窗口大小和边界
        #    窗口大小是 2*k+1。如果窗口比整个数组还大，不可能有任何有效平均值，直接返回全是-1的数组
        window_size = 2 * k + 1
        if window_size > n:
            return averages

        # 3. 使用滑动窗口高效计算
        #    - 先计算出第一个有效窗口（中心点在 k）的总和
        #    - 然后向右滑动，每次加上新进入的元素，减去滑出窗口的元素
        current_sum = sum(nums[:window_size])
        averages[k] = current_sum // window_size

        # 从第一个窗口的末尾开始遍历，向右滑动
        for i in range(window_size, n):
            # O(1) 复杂度更新窗口和：加上新元素，减去旧元素
            current_sum = current_sum - nums[i - window_size] + nums[i]
            center_index = i - k  # 计算当前窗口的中心点索引
            averages[center_index] = current_sum // window_size

# # 以中心点 c 为迭代变量的写法
# for c in range(k, n - k):
#     # 当前窗口的范围是 [c-k, c+k]
#     # ... 如何高效计算 sum(nums[c-k : c+k+1]) ?
#     # 你需要知道上一个窗口 (中心是 c-1) 的和
#     # 上一个窗口是 [c-1-k, c-1+k]
#     # 新窗口加入了 nums[c+k]，移除了 nums[c-k-1]
#     current_sum = current_sum - nums[c - k - 1] + nums[c + k]
#     averages[c] = current_sum // (2*k + 1)
        return averages

