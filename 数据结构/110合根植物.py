import sys
input = lambda :sys.stdin.readline().strip()

m,n=map(int,input().split())
k=int(input())
#并查集模板
fa=list(range(m*n+1))
def find(x):
    if fa[x]==x:return x
    fa[x]=find(fa[x])
    return fa[x]
def union(u,v):
    if find(u)!=find(v):
        fa[find(v)]=find(u)
        #并查集模板
for _ in range(k):
    u,v = map(int,input().split())
    union(u,v)

for x in range(1,m*n+1): #严格压缩成菊花图
    fa[x]=find(x)
print(len(set(fa))-1)