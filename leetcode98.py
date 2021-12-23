from binarytree import *

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# root = tree(height=2, is_perfect=False)
# print(root)
root=Node(5)
root.left=Node(1)
root.right=Node(4)
root.right.left=Node(3)
root.right.right=Node(6)
print(root)

# class Solution:
#     def isValidBST(self, root):
#         def dfs(root,left,right):
#             if not root:
#                 return True
#             elif left < root.val <right:
#                 return dfs(root.left,left,root.val) and dfs(root.right,root.val,right)
#             else:
#                 return False
#         return dfs(root,float('-inf'),float('inf'))



class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # left=float('-inf')
        # right=float('+inf')
        def dfs(node,left=float('-inf'),right=float('+inf')):

            if node is None:
                return True
            val=node.val
            # if left>=val or right<=val:
            if left<val<right:
                # return False
                if dfs(node.left,left,val) and dfs(node.right,val,right):
                    return True
            # if dfs(node.right,val,right) is False:
            #     return False
            return False
        return dfs(root)

a = Solution()
print(a.isValidBST(root))


