# 列表推导器 [expression for item in tierable if condition]

# expression 表达式 用于生成列表中的元素
# item 表示可迭代对象中的每个元素
# iterable 可迭代对象 （列表 字符串 range等）
# condition 可选条件 用于筛选元素

# 例：生成1-10的平方列表
squares = [x**2 for x in range(1,11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 例：过滤出1-20中的偶数
evens = [i for i  in range(1,21) if i%2==0]
print(evens)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 例：将输入的空格字符串列表转换为整数列表

input_data= list(map(int,input().split()))
print(input_data)

# 字符串转Map，map转列表

# 使用列表推导器来实现：
input_data=[int(x) for x in input().split()]


# 生成一个nxn的零矩阵
n = 3 
zero_matrix = [[0 for _ in range(n)] for _ in range(n)]
print(zero_matrix)
# 外层执行n次，内层执行n次，内层每次都赋值0 推导式的嵌套
# 矩阵-一个集合，是一个行列表达式
 

#  快速生成一个长度为N的斐波那契数列

# 斐波那契数列的推导式：f(n) = f(n-1) + f(n-2)
n=10
fib=[0,1]
[fib.append(fib[-1]+fib[-2]) for i in range(n-2)]
# append()-在列表末尾添加一个新元素
print(fib) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# 理解：从0 1开始，循环执行(n-2)次，每次都将前两个元素相加，添加到列表末尾

# 将二维列表展为一维列表
matrix= [[1,2,3],[4,5,6],[7,8,9]]
flatten=[x for row in matrix for x in row]
print(flatten)
# 在列表推导器中进行双层循环，从上往下，从左往右
# 从matrix中取每一行，每一行取每一个元素
# 二维矩阵的一维向量压缩

# 例：快速统计字符串中每个字符出现的次数
s="algorithm"
char_count={char:s.count(char) for char in set(s)}
print(char_count)
# 字典推导式：以char为键，s.count(char)为值 set(s)为键的集合可以去重

