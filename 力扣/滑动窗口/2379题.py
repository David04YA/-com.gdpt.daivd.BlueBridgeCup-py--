class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        #先做好题设
        n=len(blocks)
        #思路：滑动窗口，什么时候出现'W'最少，就是题目要求的最少操作次数->如何判断窗口内'W'个数？ 我会用count函数
        #特殊情况：1.k=0
        if k==0:
            return 0

        arr=[]
        min_white_count = float('inf') # 使用 float('inf') 更通用

        # 你的思路是维护一个列表作为窗口，我们来修复这个逻辑
        for i, char in enumerate(blocks):
            # 1. 入窗：将新元素加入窗口
            arr.append(char)

            # 2. 判断窗口是否形成
            # 当 i >= k-1 时，窗口长度首次达到 k
            if i >= k - 1:
                # 3. 更新结果：计算当前窗口的 'W' 数量
                # 注意：在循环内用 count() 效率不高，但我们先修复逻辑
                current_white_count = arr.count('W')
                min_white_count = min(min_white_count, current_white_count)
                
                # 4. 出窗：移除窗口最左边的元素，为下次循环做准备
                # 窗口最左边的元素永远在索引 0 的位置
                arr.pop(0)
                
        return min_white_count
