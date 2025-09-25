# 由于求符合条件的数对个数与顺序无关,先排序
# 对于 lower=<x+y<=upper,变形为 lower-x<=y<= upper-x
# 即对一个x,区间(i+1,n)中有多少个数出现在区间[lower-x,upper-x]
# 即求L=bisect(a,[lower]-x-1),R=bisect(a,upper-x)-1
      #>lower-x-1 -> >=lower-x  #>x的索引-1,只会<=x
# 如何把>=,以及<=都转换成bisect可解的模型,以上为例子
# 求出L和R的界限
# 答案即为R-L+1

from bisect import *
class Solution:
    def countFairPairs(self,a:List[int],lower:int,upper:int) ->int:
        a.sort() #sort()方法,默认升序
        res= 0 
        for i,x in enumerate(a):
            L = bisect(a,lower-x-1,i+1)
            R=bisect(a,upper-x,i+1)-1 #返回第一个大于upper-x的索引-1
            res +=R-L+1
        return res
    
#也有其他方法,如双指针