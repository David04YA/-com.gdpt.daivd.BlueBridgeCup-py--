# sorted()函数

# python内置的sorted()函数可以对任何可迭代对象进行排序，返回一个新的排序后的列表
# 基本语法：
# sorted(iterable,key=None,reverse=False)

# iterable：要排序的可迭代对象，如列表、元组、集合等
# key：可选参数，用于指定排序的依据，如lambda函数、函数名等
# reverse：可选参数，用于指定是否降序排序，默认值为False ，升序排序
# 如果为True，则降序排序

num=[1,2,3,4,5,6,7,8,9]
print(sorted(num))
print(sorted(num,reverse=True))


# 列表的sort()方法
# sort()会原地修改列表，不会返回值 不如sored方法吧
num.sort(reverse=True)
print(num)  

# 使用Lambda表达式与排序

words=['apple','banana','orange','peach']
print(sorted(words,key=lambda x:len(x)))
# lambda x:len(x) 
# x代表了words列表里的每个元素 len(x)代表了每个元素的长度

import sys

# 处理常见输入格式



# # 单行多个整数
# a,b,c = map(int,input().split())

# input()接受传入的字符串 split按照空格分割
# 然后map(int, )将分割后的每个元素转换为整数
# print(a,b,c) #print默认输出多个参数时用空格分隔

# 多行多个整数
# n = int(input()) 输入行数
# list = [int(input()) for i in range (n)]
# print(list)

# 矩阵输入
n,m = map(int,input().split()) #输入矩阵大小
# print(n,m)
matrix = [list(map(int,input().split())) for i in range(n)]#读取N行M列的矩阵
print(matrix)

# 实际上m没有被使用到