#因为从1开始编号,所以要将数组的每个元素都加
#第一次出现的位置->恰好>=q的位置->恰好>q--1的位置

from bisect import *
import sys
input = lambda :sys.stdin.readline().strip()
n,m = map(int,input().split())
nums= list(map(int,input().split()))
Q=list(map(int,input().split()))

s=set(nums)#nums构成的积和,如果待查询的数组q not in s,直接返回-1
for q in Q:
    if q not in s:
        print(-1,end=" ")
        #结尾符缺省的是一个换行
    else:#q一定出现在nums中,利用技巧将"大于等于x"转化为"大于x-1"
        print(bisect(nums,q-1)+1,end=" ")
