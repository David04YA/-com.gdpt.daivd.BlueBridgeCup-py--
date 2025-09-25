import sys
imput = lambda: sys.stdin.readline().strip()

n=int(input())
a,b = zip(*[map(int,input().split()) for _ in range(n)])
# zip(*...)如果读入的数据是 [[10, 3], [20, 6]]
# ，它会把第一列的数 [10, 20] 和第二列的数 [3, 6] 分开，
# 分别存到变量 a 和 b 里
#用zip打包成元组列表
def bisect(lo,hi,target,check):
    while lo<hi:
       mid=(lo+hi)>>1
       if check(mid):
           hi=mid
       else:
           lo=mid+1
    return lo
m=bisect(1,10**9,lambda v:all(A//v<=B for A,B in zip(a,b)))
M=bisect(1,10**9,lambda v:any(A//v>B for A,B in zip(a,b)))-1
print(m,M)