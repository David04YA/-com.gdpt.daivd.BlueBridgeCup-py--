# # 扩展：如果有 n 个节点要怎么做？（Python/Java/C++/C/Go/JS/Rust）
# 把题目扩展一下：设二叉树上有 n 个节点（n≥3），且每个节点都有 0 或 2 个儿子。要求判断除了叶子节点，是否每个节点的值都等于其左右儿子的节点值之和。

# 这可以用递归解决，请看 深入理解递归【基础算法精讲 09】，思路如下：

# 如果当前节点是叶子节点，直接返回 true，表示无需判断叶子。
# 否则，如果当前节点的节点值不等于其儿子的节点值之和，返回 false。
# 否则，递归左右儿子，如果它们都返回 true，那么当前节点返回 true，否则返回 false。

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/root-equals-sum-of-children/solutions/2396139/kuo-zhan-ru-guo-you-n-ge-jie-dian-yao-ze-eevi/
# 来源：力扣（LeetCode）
# # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        # 递归边界1: 如果当前节点是 None，根据题目定义（有效树的一部分），可以安全地返回 True
        if root is None:
            return True
        # 递归边界2: 如果当前节点是叶子节点，它满足条件，返回 True
        if root.left is None and root.right is None:
            return True
        # 检查：如果节点结构不符合“同时有左右子节点”的假设，则不满足条件
        if root.left is None or root.right is None:
            return False
        # 递归检查：当前节点值是否等于子节点之和，并且左右子树也满足条件
        return (root.val == root.left.val + root.right.val) and \
               self.checkTree(root.left) and self.checkTree(root.right)
        

        #self.checkTree(root.left)调用了checkTree方法，但传入了更小部分作为参数
        # 这种在函数内部调用自己的行为，就是递归