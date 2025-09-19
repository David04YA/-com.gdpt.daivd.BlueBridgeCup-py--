from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        # 1. 定义一个元音集合，使用集合(set)进行判断效率更高
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # 2. 初始化计数器
        count = 0
        
        # 3. 遍历指定的 [left, right] 范围
        for i in range(left, right + 1):
            # 获取当前单词
            word = words[i]
            
            # 4. 判断条件：
            # - 单词的第一个字符 (word[0]) 在元音集合中
            # - 并且单词的最后一个字符 (word[-1]) 也在元音集合中
            # Python的负数索引 -1 可以方便地获取最后一个元素
            if word[0] in vowels and word[-1] in vowels:
                # 5. 如果满足条件，计数器加 1
                count += 1
                
        # 6. 循环结束后，返回总数
        return count
