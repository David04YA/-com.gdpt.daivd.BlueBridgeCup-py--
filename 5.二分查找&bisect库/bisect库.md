from bisect import *
#
然后直接调用bisect()函数即可

# 示例函数
arr= [1,9,9,9,200,500]

# 查询插入位置
print(bisect(arr,0)) #输出:1(第一个大于3的索引)
print(bisect(arr,9)) #输出:4(第一个大于等于9的索引)

 bisect库二分查找
 bisect(a,x,lo=0,hi=len(nums))
 给定一个单调不减的数组a,在其[lo,hi)区间内,返回第一个严格大于x的下标位置
 a是传入的数组 x是要查找的目标值 lo是查找的起始位置 hi是查找的结束位置,默认是数组的长度
 时间复杂度O(logn) 
 # 通过二分,让每次查找的长度变为原来的一半


# bisect_left()是一个>=的查找 可以用x=x-1代替
