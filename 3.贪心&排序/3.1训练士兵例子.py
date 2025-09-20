# 1.语言整理: 共n人,每人训练Ci次,没人单独训练每次花费Pi元,团练训练花费S元.求所有人完成训练的最少花费
# 读题中要把不相关的字眼删除然后整理

# 思路:
# 团购价不变,有的人训练数ci少,有些人多
# 一开始团购价S比所有人单独价格total更小,随着有人完成后推出,total应该动态更新维护
# 当团购不合适S>total时,单独操作 联想到贪心+排序,尽可能多的贪心,讨论所有人需要训练的次数,从小到大排序

# 从小到大,对这个升序序列进行遍历,对次数小的人就应该优先团购,剩下的人单独训练

# 去记录一共团购多次,总次数减去团购次数就是单独次数
# tot初始为∑Pi 所有的P值加起来的综合,求和符号
# 用res记录答案 初始为0,用count记录已经团购的次数
#res<-res+(Ci-cnt)XS (总共训练的次数-团购次数)x价格;cnt<-Ci Ci至少不会比cnt小,用当前的C更新就好
# 如果团购不合适:res <- res +(Ci- cnt)xPi Pi使用的时候,团购已经不合适了,同时count值也不更新,因为不用团购了
# 同时每次遍历完成代表一个人训练完成且退出,后续就不用考虑他了,需要动态维护total
# tot<-tot-Pi
nums=[[0,0]] * n  #用于排序
p,c=[0]*n,[0]*n
for i in range(n):
    nums[i]=list(map(int,input().split())) #按照训练的次数升序排序(默认)
    # 把排序后的结果赋值给p和c p是价格 c是次数
    for i in range(n):
        p[i]=nums[i][0]
        c[i]=nums[i][1]
    tot=sum(p) #total定义为P的总和
    res=0
    count=0
    #按照训练次数升序遍历,若tot>=S,团购合适:
    # res<-res+(Ci-cnt)XS; cnt <-Ci
    for i in range(n):
    if tot>=s:
        res+=(c[i]-count)*s
        count=c[i]
    else: #否则团购不合适,res<-res+(Ci-cnt)XPi 此人单独训练
        res += (c[i]-cnt)*P[i]
    tot -= P[i] #第i人完成训练,减去他的单独总成本
    print(res)
 
