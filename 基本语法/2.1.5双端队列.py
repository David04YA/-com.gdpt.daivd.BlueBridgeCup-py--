# 应用场景:
# 队列：BFS层序遍历、滑动窗口等
# 栈：DFS路径回溯、括号匹配、单调栈优化

# 双端队列：只允许从两端插入，两端删除的线性表
# 队列：只允许一段插入，另一端删除的线性表
# 栈：只允许一段插入和删除的线性表

# 队列（先进先出）
from collections import deque

q=deque()
q.append(x)#从右侧入队
q.appendleft(x)#从左侧入队
q.pop()#从右侧出队
q.popleft()#从左侧出队
len(q)#队列长度

# 栈（先进后出）
stk=[]
stk.append(x)#入栈
stk.pop()#出栈
stk[-1]#栈顶元素

# 技巧：
# 快速判断空队列/栈：
#  if not q:

# 栈的反转：stack[::-1] 用切片获取逆序，切片生成一个新序列，不会改原始数据
# 队列转列表：list(q)

# 迭代器初始化：deque([1,2,3])