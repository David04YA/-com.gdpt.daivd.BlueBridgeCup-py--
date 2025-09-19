class Solution:
    def maxScore(self, s: str) -> int:
        """
        解题思路（暴力解法）:
        直接模拟题目的要求：遍历每一个可能的分割点，计算得分，然后取最大值。
        """
        # 1. 初始化一个变量来存储最大得分
        max_score = 0
        
        # 2. 遍历所有可能的分割点 i
        # i 的范围从 1 到 len(s)-1，这样可以确保左右子串都不为空。
        # 当分割点为 i 时, 左子串是 s[0:i]，右子串是 s[i:]。
        for i in range(1, len(s)):
            # 3. 分割字符串
            left_substring = s[0:i]
            right_substring = s[i:]
            
            # 4. 计算当前分割的得分
            # 得分 = (左子串中'0'的数量) + (右子串中'1'的数量)
            # 使用字符串的 .count() 方法来计数
            current_score = left_substring.count('0') + right_substring.count('1')
            
            # 5. 更新最大得分
            # 如果当前得分比记录的最大得分要高，就更新它
            # 也可以用 max_score = max(max_score, current_score)
            if current_score > max_score:
                max_score = current_score
                
        # 6. 循环结束后，返回找到的最大得分
        return max_score