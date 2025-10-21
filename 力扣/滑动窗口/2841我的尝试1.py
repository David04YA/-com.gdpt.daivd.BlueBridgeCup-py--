class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        #考虑特殊情况1.k直接为0，不存在子数组
        if k == 0:
            return 0
        #互不相同元素的判断： 创造一个列表存储前面的值，if nums[i] in arr ，那么统计个数count-1 然后做判断，是否count=m，如果等于m，那令其和=temp，temp和final比较大小更新
        m_count=0
        temp_sum=final_sum=0
        n=len(nums)
        arr=[]
        #考虑特殊情况2.还未形成第一个窗口时，长度k值过大导致根本不存在子数组。
        if k>n:
            return 0
        #存储值到列表中
        for i,j in enumerate(nums[0:k]):
            if j not in arr:
                m_count +=1
            arr.append(j)
        if m_count == m:
            temp_sum=final_sum=sum(nums[0:k])
        #第一个窗口判断完了，接下来该滑动了         
        for i,j in enumerate(nums[k:n]):
            #先滑出arr的左端点，不然arr会一直累加，互不相同的窗口从[L,i]变成[0,n]，先判断这个滑出的端点在arr中互不相同吗？如果互不相同，它滑出了就得count-=1
            # if arr[0] not in arr[1:]:
            # 如果窗口是 [1, 2, 3]，滑出 1，arr[1:] 是 [2, 3]，1 不在 [2, 3] 中，m_count 减一，这也是对的。
            # 那问题出在哪？问题在于，当窗口是 [1, 1, 2] 时，滑出 arr[0] (也就是 1)，arr[1:] 是 [1, 2]，1 仍然在 [1, 2] 中，所以 m_count 不会减一。但实际上，我们只是移除了一个 1，窗口里还有一个 1，不同元素的总数并没有变化。所以这个判断逻辑本身就不够健壮。
                m_count -= 1
            arr.pop(0)
            #新加入的是右端点i,判断是否在arr中相同
            if j not in arr: #时间复杂度变高 O(n*k)
                m_count += 1
            arr.append(j)
            if m_count == m: #>=
                #这里的区间，长度为k，右端点是i 根据[L,R] K 有R-L+1=K L=R-K+1 在本题中左端点L=i-k+1
                temp_sum= sum(nums[i-k+1:i]) #又是一个O(k)操作
                final_sum=max(temp_sum,final_sum)
        return final_sum
            

# 列表 arr 来模拟窗口用 if j not in arr每次判断，Python 都需要从头到尾检查一遍 arr 列表，非常慢。
#哈希表（字典）-dict  键 (Key)：学生的姓名（在我们的代码里，就是数组中的数字 nums[i]）。
# 值 (Value)：这个学生被点到了几次（在我们的代码里，就是这个数字在窗口中出现了多少次）。 
# 能以接近 O(1) 的超快速度直接定位到某个“键”。