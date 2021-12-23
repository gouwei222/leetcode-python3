from binarytree import *
from collections import *
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
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#         else:
#             return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue=[root]
        i=0
        while queue:
            tmp=[]
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue=tmp
            i+=1
        return i
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#         q = deque([root])
#         level = 0
#         while q:
#             n = len(q)
#             for i in range(n):
#                 node = q.popleft()
#                 if node.left is not None:
#                     q.append(node.left)
#                 if node.right is not None:
#                     q.append(node.right)
#             level += 1
#         return level



a=Solution()
print((a.maxDepth(p)))