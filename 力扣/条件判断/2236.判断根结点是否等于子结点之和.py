# 2236. 判断根结点是否等于子结点之和
# 简单
# 相关标签
# premium lock icon
# 相关企业
# 给你一个 二叉树 的根结点 root，该二叉树由恰好 3 个结点组成：根结点、左子结点和右子结点。

# 如果根结点值等于两个子结点值之和，返回 true ，否则返回 false 。

 

# 示例 1：


# 输入：root = [10,4,6]
# 输出：true
# 解释：根结点、左子结点和右子结点的值分别是 10 、4 和 6 。
# 由于 10 等于 4 + 6 ，因此返回 true 。
# 示例 2：


# 输入：root = [5,3,1]
# 输出：false
# 解释：根结点、左子结点和右子结点的值分别是 5 、3 和 1 。
# 由于 5 不等于 3 + 1 ，因此返回 false 。
 

# 提示：

# 树只包含根结点、左子结点和右子结点
# -100 <= Node.val <= 100

# Definition for a binary tree node.
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        # 对于这道题，题目保证了 root, root.left, root.right 都不会是 None
        # 所以下面的简洁写法是安全且正确的。
        # return root.val == root.left.val + root.right.val

        # 在更通用的场景下，为了防止 'AttributeError'，需要先进行检查。
        # 这是一个更健壮的写法：
        if root and root.left and root.right:
            return root.val == root.left.val + root.right.val
        return False # 如果节点不完整，则返回 False
    
    # 这里注意root.val是获取根节点的值，root.right和root.left都是获取的子树，我们先获取左右子树，把它们当成一个新的二叉树，然后再.val就可以获取对应左右子树根结点的值