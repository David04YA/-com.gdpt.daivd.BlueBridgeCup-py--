# 埃氏筛
# 对2到N-1的所有数遍历一遍，傻瓜办法
# 时间复杂度证明：Mertens第二定理
# 任何一个素数的倍数，说明存在另一个因子，一定不是素数
# 切片优化
import math
n=int(input("请输入一个数字："))
primes = []
#primes 存取每一个素数的列表
is_prime=[True]*(n+1)
#is_prime 判断一个数是不是素数的列表

for i  in range(2,int(math.sqrt(n)+1)):
    #从2开始进行遍历
    if is_prime[i]:
        #如果一个数是素数，把所有的倍数都划掉
        for j in range(i*i,n+1,i):
            #步长为什么是i-筛选出所有素数i倍数
            # 为什么从i平方开始-避免和之前的素数重复
            is_prime[j]=False #把所有的倍数都划掉
for i in range(2,n+1):
    if is_prime[i]:
        primes.append(i)
#从2开始，一直遍历到n，把所有的素数都筛选出来
print(primes)
