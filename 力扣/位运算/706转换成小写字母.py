    # 709. 转换成小写字母
    # 已解答
    # 简单
    # 相关标签
    # premium lock icon
    # 相关企业
    # 提示
    # 给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。

    

    # 示例 1：

    # 输入：s = "Hello"
    # 输出："hello"
    # 示例 2：

    # 输入：s = "here"
    # 输出："here"
    # 示例 3：

    # 输入：s = "LOVELY"
    # 输出："lovely"
    

    # 提示：

    # 1 <= s.length <= 100
    # s 由 ASCII 字符集中的可打印字符组成

# 法1.直接调用API
# class Solution:
#     def toLowerCase(self, s: str) -> str:
#         return s.lower()
    
class Solution:
    def toLowerCase(self, s: str) -> str:
     return "".join(chr(asc | 32) if 65 <= (asc := ord(ch)) <= 90 else ch for ch in s)
# for ch in s 遍历s字符串中的每一个字符ch，ch会执行括号内的所有逻辑

# 三元条件表达式 value if true if condition else value if false
# ord()函数-获取ASCII码值
# asc:=ord(ch) 将值赋给asc

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/to-lower-case/solutions/1151839/zhuan-huan-cheng-xiao-xie-zi-mu-by-leetc-5e29/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。