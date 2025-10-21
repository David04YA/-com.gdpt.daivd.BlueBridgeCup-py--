lass Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 特殊情况处理
        if k == 0:
            return 0

        # 1. 初始化：计算第一个窗口（前 k 个字符）中 'W' 的数量
        #    我们用 current_white_count 来追踪当前窗口的 'W' 数量
        current_white_count = blocks[:k].count('W')
        
        # min_white_count 用于记录滑动过程中遇到的最少 'W' 数量
        min_white_count = current_white_count

        # 2. 滑动窗口：从第 k 个字符开始遍历，作为新进入窗口的字符
        #    此时窗口的范围是 [i - k + 1, i]
        for i in range(k, len(blocks)):
            # 加上新进入字符的影响
            if blocks[i] == 'W':
                current_white_count += 1
            
            # 减去滑出窗口字符的影响
            # 滑出窗口的字符索引是 i - k
            if blocks[i - k] == 'W':
                current_white_count -= 1
            
            # 3. 更新结果：每次滑动后，都比较并保留最小的'W'数量
            min_white_count = min(min_white_count, current_white_count)
            
        return min_white_count

# 这个方法避免了在循环中反复使用 arr.count('W') 和 arr.pop(0)，将时间复杂度从 O(n * k) 优化到了 O(n)，这足以通过所有测试用例。