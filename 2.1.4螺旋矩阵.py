# 生成螺旋矩阵（复杂索引控制）
n = 3
matrix = [[0] * n for _ in range(n)]
# [0] * n: 这部分会创建一个包含 n 个 0 的列表。
# 重复执行‘创建一个包含n个0的列表’这个动作n次
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# (0,1)行不变，列+1 向右 
# (1,0)列不变，行+1 向下
# (0,-1)行不变，列-1 向左
# (-1,0)列不变，行-1 向上
x,y,num,d = 0,0,1,0
for step in range(n,0,-2):
    #从n开始，每次递减2的序列，例如n=3时，序列为[3,1]
    for i in range(4 if step > 1 else 1):
        dx,dy = direction[d]
        for i in range(step - 1):
            matrix[x][y] = num
            num += 1 
            x += dx
            y += dy
        d = (d + 1) % 4
print(matrix)
   
# 数字从 1 开始，从矩阵的左上角出发
# 按照顺时针方向，像螺旋一样依次填充整个矩阵，如下：
# [[1, 2, 3],
#  [8, 9, 4],
#  [7, 6, 5]]