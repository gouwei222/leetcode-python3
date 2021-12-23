from binarytree import *
p=Node(1)
p.left=Node(2)
p.right=Node(3)
# p.right.left=Node(4)
print(p)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) :
        ret=[]
        queue=[root] #用来存每一层的节点
        if root is None:
            return []
        while queue:
            tmp=[]
            ret.append([node.val for node in queue])
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue=tmp
        return ret
a=Solution()
print(a.levelOrder(p))


# from collections import deque
#
# class Solution:
#     def levelOrder(self, root):
#         ret = []
#         queue = deque([root])
#         while queue:
#             tmp = []
#             for i in range(len(queue)):
#                 point = queue.popleft()
#                 if point:
#                     tmp.append(point.val)
#                     queue.append(point.left)
#                     queue.append(point.right)
#             if tmp:
#                 ret.append(tmp)
#         return ret
