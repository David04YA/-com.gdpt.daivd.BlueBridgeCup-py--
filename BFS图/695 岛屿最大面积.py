# 思路:
# 1.枚举每个联通的岛屿,通过将访问过的位置设置为0,即grid[i][j]=0进行记录
# 2.每个岛屿的登陆点即为q的初始内容
# 3.每次将q的队首弹出,考虑其上下左右是否有陆地,是则加入到队尾,并标记访问过,更新岛屿面积
# 4.重复操作直到q为空
from collections import deque
from typing import List
def maxAreaOfIsland(self,g:List[List[int]])->int:
    #g:一个01矩阵 传入的岛屿列表
    n,m=len(g),len(g[0]) 
    # g是一个list,而g里面又包含着数组,当我写下n=len(g)时,代表获取list总长度
    # 写下m=len(g[0])时,代表我获取list中每一个数组的长度
    res=0
    di=[(0,1),(0,-1),(1,0),(-1,0)]
    def bfs(i,j):
        ans = 1 #初始面积为1
        q=deque([(i,j)]) #考虑登陆点(i,j)的岛屿 (i,j)入队
        g[i][j]=0 #标记访问过
        while q: #q不为空就一直执行
            x,y=q.popleft() #从左侧弹出  
            for dx,dy in di: #考虑四个方向
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and g[nx][ny] == 1: #合法且为陆地
                    q.append((nx,ny))
                    ans +=1
                    g[nx][ny]=0 #标记访问过 
        return ans
    for i,row in enumerate(g):
        for j,x in enumerate(row):
            #从左上到右下的辨定顺序,每次都只考虑一个岛屿
            if x == 1:
                res=max(res,bfs(i,j)) #更新
    return res