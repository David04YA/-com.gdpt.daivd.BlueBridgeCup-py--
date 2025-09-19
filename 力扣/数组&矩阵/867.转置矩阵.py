# # 第一次尝试：class Solution:
# #     def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
# #         #定义一个新矩阵来返回值
# #         m = int(matrix.length)
# #         n = int(matrix[i].length)
# #         res_M=[]
# #         for i in range(n):
# #             for j in range(m):
# #                 res_M[i,j]=matrix[m,n]
# #         return res_M

# # 矩阵转置的核心思想：创建一个新的矩阵，然后将原矩阵的 (j, i) 位置的元素放到新矩阵的 (i, j) 位置。

# # 在 Python 中，获取列表（也就是这里的行数）的长度应该使用内置函数 len()，而不是 .length 属性

# # res_M=[]：这里你只是创建了一个空列表。当你稍后尝试用 res_M[i,j] 访问时，因为这些位置还不存在，程序会抛出 IndexError（索引越界）的错误。我们需要先创建一个 n 行 m 列的矩阵结构。

# 访问和赋值元素:

# res_M[i,j]=matrix[m,n]：
# 在 Python 中，访问二维列表的元素需要用两个方括号 list[row][col]，而不是 list[row, col]。
# 核心逻辑应该是 res_M[i][j] = matrix[j][i]。你写的 matrix[m,n] 是想用矩阵的维度 m 和 n 去访问元素，这会超出索引范围。