import math

# “埃拉托斯特尼筛法”（Sieve of Eratosthenes）找出所有小于等于 MAX_N 的素数
MAX_N = 100  # 示例：找出100以内的所有素数

# 1. 创建一个布尔列表，用于标记数字是否为素数。
#    初始化所有值为 True。列表大小为 MAX_N + 1，以便索引可以直接对应数字 0 到 MAX_N。
is_prime = [True] * (MAX_N + 1)

# 2. 0 和 1 不是素数，手动标记为 False。
is_prime[0] = is_prime[1] = False

# 3. 从 2 遍历到 sqrt(MAX_N)。
#    外层循环只需要到 sqrt(MAX_N) 即可，因为任何大于 sqrt(MAX_N) 的合数，
#    都必然有一个小于 sqrt(MAX_N) 的素因子，在之前的循环中已经被划掉了。
for i in range(2, int(math.sqrt(MAX_N)) + 1):
    # 如果 i 是一个素数（即它还没有被标记为 False）
    if is_prime[i]:
        # 那么 i 的所有倍数都不是素数，将它们标记为 False。
        # 我们可以从 i*i 开始标记，这是一个优化。
        # 因为像 2*i, 3*i 这样更小的倍数，一定已经被更小的素数（如 2, 3）标记过了。
        # 例如，当 i=5 时，2*5=10 已被 2 标记，3*5=15 已被 3 标记。我们直接从 5*5=25 开始即可。
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False

# 4. 筛选结束后，所有仍然标记为 True 的数字的索引，就是素数。
#    我们可以用列表推导式来收集所有结果。
primes = [i for i, is_p in enumerate(is_prime) if is_p]

print(f"{MAX_N} 以内的素数有:")
print(primes)

# math.sqrt 计算平方根
# 定理：如果一个数n是合数，那么它必定有一个因子≤√n
# 解释：对于任意一对因子 a * b = n，必然有一个因子≤√n，另一个因子≥√n。
# 所以，如果一个数n不是素数，那么它必定有一个小于或等于√n的因子。
# 因此，在【判断单个数字是否为素数】时，我们只需要检查2到√n之间的数是否是n的因子即可。

