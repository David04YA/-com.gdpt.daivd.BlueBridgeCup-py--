class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:):
     #哈希和前缀和 
     #很直观的做法,对这个数组列表遍历每一个数,同时遍历其他的数,若两数之和等于target,则返回
    #计算时间复杂度:看循环
    # 其他语句块可以认为是O(1)常数级别-与N无关
        n=len(nums)
        for i in range(n):
            #要排除一个数用两次
            for j in range(n):
                if i== j:continue
                #continue跳出一次 break 跳出当前循环块
            x,y=nums[i],nums[j]
            if x + y ==target:
                return [i,j]
            # 对于这个循环 可以认为 n* n* 1 = O(n^2) n= 10^4,一个代码要通过一般在10^8左右

            # 优化:题目要求可以按任意顺序返回答案
            #i=1,j=2 i=2,j=1 同样的情况考虑了两遍 只进行一次计算就可以了 
            #j>i这个冗余要去掉
            for i in range(n):
                for j in range(i+1,n): #循环次数缩小了一半的复杂度
                    if x + y ==target:
                        return [i,j]
                    
                    # 对于 x,满足x+y = target 则 Y=target -x target已知,x已知,则y也已知
                    # 如何快速判断y是否存在
                    # 举例 x= 2,往后去找是否存在一个值+x = target
                    # 1.在考虑值时,只考虑x后面的,这就是刚才做的i+1
                    # 有没有办法看它的前缀,同时前缀的信息是已知的,有没有办法把前缀信息存储,同时在O(1)级别内把信息获取出来

                    n = len(nums)
                    d={} #{key 数字,value 下标}
                    #O(1)
                    #for index,item in enumerate()
                    for i,x in enumerate(nums):
                        # 对x考虑nums[:i] 在这个区间内是否存在y ,y=target - x
                        # 原本的方法是i+1,想要查找只能循环到索引末端,任何算法都不能未卜先知,不查找就知道
                        # 所以我们把索引和数值存储,存完后再在字典里查找
                        # 怎么去查这个字典-target-x 数字 我们查到的东西是下标
                        #记录已经出现过的键值对 数值-下标对
                        d[x]=i
                        if d.get(target-x) is not None:
                            return[i,d[target-x]]
                        
                        
                        #记录下来已经存在的值
                        #hash哈希思想 定义一个字典 dict d={} get方法 d.get(key,default_value=None)
                        # 前缀哈希-对前缀进行维护,一边遍历一边更新
                        # 获取key对应的值,如果不存在返回None
                        # keys() values() 两个方法获得可迭代对象
                        # d[key]=value

