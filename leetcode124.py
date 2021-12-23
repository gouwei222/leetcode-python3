#二叉树中最大路径和
from binarytree import *
p=Node(3)
p.left=Node(9)
p.right=Node(20)
p.right.left=Node(15)
p.right.right=Node(7)
# p.right.left=Node(4)
print(p)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        self.ret=root.val
        def dfs(root):
            if root is None:
                return 0
            left=max(0,dfs(root.left))
            right=max(0,dfs(root.right))
            self.ret=max(self.ret,root.val+left+right)
            return root.val+max(left,right)
        dfs(root)
        return self.ret
a=Solution()
print(a.maxPathSum((p)))