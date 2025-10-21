class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        #返回值：数组avgs 要定义好数组长度 根据题设，每个i都有
        avgs=[-1]*n
        #滑动窗口 中心点为i，left=i-k,right=i+k,总滑动2k 1
        temp=0
        window_size=2*k+1
        for i,j in enumerate(nums):
            #越界考虑
            #1.窗口比整个数组都大了 win>len
            #2.半径k=0 k==0
            #3.i前或i后不足k个元素了 
            #前不足k i<k不执行 后不足k i+k>n
            if window_size >n:
                return avgs
            if k==0:
                return nums
            if i<k:
                avgs[i]=-1
                continue
            if i+k>n:
                avgs[i]=-1
                continue
            temp=sum(nums[i-k:i+k])
            avgs[i]=temp//window_size
            temp -= nums[i-k]
            if i+k<n:
                temp += nums[i+k]
                #滑动逻辑不行：在本轮循环中，temp和avg的计算已经完成，最后才进行滑动尝试，反而根本不影响本轮运算结果。
                #我们该做的： 能不能将滑动尝试提前?(在这种写法中) 当然是不行的，因为若（在这种写法中）提前滑动，那么会导致对于第一个 中心点i 有 ：他的左端点减一，右端点加一
                #这会导致avg[i_1]的值不准确 在i_2中并不会影响，下轮是下轮的事（这种写法中）
                #我们的新写法：首次计算不进入循环，从第二次开始才进入循环
            else:
                continue
        return avgs