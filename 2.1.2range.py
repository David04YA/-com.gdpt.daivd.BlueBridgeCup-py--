# range函数
# range(start,stop,step)
# start 序列的起始值，默认为0
# stop 序列的结束值，不包含在序列中
# step 序列的步长，默认为1

# range返回的是一个range对象，是一个惰性序列，节省内存
#是一个可迭代对象 如果需要列表，可以用List()函数将range对象转换为列表

seq = range(10)
print(list(seq))

# 生成1-10的奇数序列（步长测试）
odd_seq = range(1,11,2)
print(list(odd_seq))

# 生成倒序序列
seq = range(10,0,-1)
# 左闭右开
print(list(seq))

# 生成循环的索引（模运算结合）
# 希望生成0-4 重复变成0的索引，重复两次
# 对具体的索引值取模n后赋值给nindex，就会变成0，1，2，3，4，0，1，2，3，4
# 实现了循环的效果

n= 5
for i in range(n*2):
    nindex = i%n
    print(nindex)

# 生成二维网格坐标（嵌套循环）以下为例子
rows,cols=2,3
grid = [[i,j] for i in range(rows) for j in range(cols)]
print(grid) # [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]]