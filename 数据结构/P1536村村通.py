import sys
input = lambda :sys.stdin.readline().strip()
 
while True:
    s=input()
    if s =='0':break
    n,m=map(int,s.split())
    fa=list(range(n+1))
    def find(x):
        if fa[x]==x:return x
        fa[x]=find(fa[x])
        return fa[x]
    def union(u,v):
        if find(u)!=find(v):
            fa[find(v)]=find(u)
    for _ in range(m): #对总共的m条边，进行union操作，用集合的合并来转换边的连通性思想
        u,v=map(int,input().split())
        union(u,v)

    #压缩成严格菊花集，防止出现父级节点没有指向根的情况
    for x in range(1,n+1):
        fa[x]=find(x) #令fa[x]=根节点
    
    cnt=len(set(fa))-1 #-1是因为下标从1开始，但前面把0也算了进去
     #set()创建一个集合，因为集合的唯一性，当用set(fa)存储fa这个列表时，自动你去除所有重复的根节点
    print(cnt-1) #如果有cnt个连通块，就需要cnt-1条边新增