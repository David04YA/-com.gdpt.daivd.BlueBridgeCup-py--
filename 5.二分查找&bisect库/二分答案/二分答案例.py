#需要找到一个单调增函数f(x)=x^3+x+1在区间[1,10^18]上恰好满足check(x)=f(x)>target为True的临界点
# 可以利用单调性，对x在区间上二分，找出恰好满足check(x)=True的临界点

def f(x):
    return x**3+x+1
def bisect(lo,hi,target,check):
    while lo<hi:
        i = (lo+hi)>>1
        if check(i,target):
            hi=i
        else:
            lo=i+1
    return lo

target= 9999
res = bisect(1,10**18,target,lambda x,target:f(x)>target)
print(res)
print(f(res))
print(f(res-1))