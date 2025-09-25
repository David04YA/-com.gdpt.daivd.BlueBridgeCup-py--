#k=2表示两次蔓延，这题要求进行K次蔓延
#BFS网格题是有一些生活规律的题目

import sys
from collections import deque #双端队列
input = lambda: sys.stdin.readline().strip()
n,m=map(int,input().split())
g=[[0]*m for _ in range(n)] #把一个字符串构成的列表转换成01矩阵

di=[(0,1),(0,-1),(1,0),(-1,0)]
q = deque() #双端队列
for i in range(n):
    r=input() #接受一行字符串
    
    for j,x in enumerate(r):
        #例子当i=0,j=2时，找到了一个字符g，更新到g[0][2]=1，并将(0,2)加入队列 预处理思想
        if x =='g':
            g[i][j]=1 #把g矩阵中对应(i,j)位置更新为1
            q.append((i,j)) 
k=int(input())
while k and q:
    for _ in range(len(q)): #表示当前蔓延过程中，有多少个元素就代表了有多少颗草
        x,y=q.popleft() #队首位置的元素弹出
        for dx,dy in di: #遍历
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and g[nx][ny]==0: #考虑是否越界且是否为0
            
                g[nx][ny]=1
                q.append((nx,ny)) #加入队尾位置
                #不用像上一题一样做标记访问，因为已经做了预处理，而且上一题是二重循环，左上到右下的遍历，我们希望在
                #遍历到其他位置时不要再考虑已经访问过的位置，所以要标记访问然后删除
                #这里不需要，因为这里的所有初始值是一个静态的队列，所有的g=1的位置都已经入队了，不是一个动态的获取过程
              
    k-=1
for row in g: #还原成字符串输出
        print(''.join('g' if x else '.' for x in row))
        #''.join函数: .join前的是分隔符
        # 传入参数-一个可迭代对象


 