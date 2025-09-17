# 1534. 统计好三元组
# 简单
# 相关标签
# 高级锁图标
# 相关企业
# 提示
# 给你一个整数数组 ，以及 、 、 三个整数。 请你统计其中好三元组的数量。arrabc

# 如果三元组 满足下列全部条件，则认为它是一个 好三元组 。(arr[i], arr[j], arr[k])

# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# 其中 表示 的绝对值。|x|x

# 返回 好三元组的数量 。

 

# 示例 1：

# 输入：arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# 输出：4
# 解释：一共有 4 个好三元组：[(3,0,1), (3,0,1), (3,1,1), (0,1,1)] 。
# 示例 2：

# 输入：arr = [1,1,2,2,3], a = 0, b = 0, c = 1
# 输出：0
# 解释：不存在满足所有条件的三元组。
 

# 提示：

# 3 <= arr.length <= 100
# 0 <= arr[i] <= 1000
# 0 <= a, b, c <= 1000
import typing
from typing import List
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # 1. 定义一个计数器，初始为 0，用来记录好三元组的数量
        count = 0
        # 2. 获取数组的长度
        n = len(arr)

        # 3. 使用三重循环来生成所有满足 0 <= i < j < k < n 的三元组
        # 最外层循环遍历 i
        for i in range(n):
            # 中间层循环遍历 j，从 i+1 开始以保证 i < j
            for j in range(i + 1, n):
                # 最内层循环遍历 k，从 j+1 开始以保证 j < k
                for k in range(j + 1, n):
                    # 4. 检查三元组是否满足所有三个条件
                    if abs(arr[i] - arr[j]) <= a and \
                       abs(arr[j] - arr[k]) <= b and \
                       abs(arr[i] - arr[k]) <= c:
                        # 如果所有条件都满足，计数器加 1
                        count += 1
        
        # 5. 所有循环结束后，返回最终的计数结果
        return count

# --- 本地测试入口 ---
# 这部分代码只有在直接运行这个 .py 文件时才会执行
# 在 LeetCode 平台上，这部分代码会被忽略
if __name__ == "__main__":
    # 1. 实例化你的 Solution 类
    # 创建一个 Solution 类的对象，这样我们才能调用它的方法
    solution = Solution()

    # 2. 准备要传递的参数 (实参)
    # 对应示例 1 的数据
    test_arr = [3, 0, 1, 1, 9, 7]
    test_a = 7
    test_b = 2
    test_c = 3

    # 3. 调用方法，并把准备好的参数传递进去
    result = solution.countGoodTriplets(test_arr, test_a, test_b, test_c)

    # 4. 打印结果，看看是否和预期一致
    print(f"测试数组: {test_arr}")
    print(f"参数 a={test_a}, b={test_b}, c={test_c}")
    print(f"找到的好三元组数量是: {result}") # 应该输出 4
