# [朴素二分]实现bisect
def bisect(a,x,lo=0,hi=None):
    # 初始值给一个none在赋值len(a)，不然无法执行
    if hi is None:hi=len(a)
    while lo<hi:
        i = (lo+hi)>>1
        #>>1 二进制右移一位，相当于数值//2然后向下取整
        if a[i]>x:
            hi=i
        else:
            lo=i+1
    return lo