import math
primes=[]
is_prime = [True]*(primes+1) #最大可能遇到的质数+1
is_prime[0]=is_prime[1]=False

for i in range(2,int(math.sqrt(primes))+1):
    if is_prime[i]:
       for j in range(i*i,i+1,i):
           is_prime[j]=False
for i in range(2,i+1):
    if is_prime[i]:
        primes.append(i)

# math.sqrt 计算平方根
# 定理：如果一个数n是合数，那么它必定有一个因子≤√n
# 对于任意一对因子a x b = n，必然有一个因子≤√n，另一个因子≥√n
# 所以如果一个数n不是素数，那么它必定有一个因子≤√n
# 所以我们只需要检查2到√n之间的数是否是n的因子即可
