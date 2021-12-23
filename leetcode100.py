from binarytree import *
p=Node(1)
p.left=Node(2)
p.right=Node(3)
# p.right.left=Node(4)
print(p)

q=Node(1)
q.left=Node(2)
q.right=Node(3)
# p.right.left=Node(4)
print(q)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         def dfs(p, q):
#             if not p and not q:
#                 return True
#             elif not p or not q:
#                 return False
#             elif p.val == q.val:
#                 return dfs(p.left, q.left) and dfs(p.right, q.right)
#             else:
#                 return False
#
#         return dfs(p, q)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#################breeze######################
from collections import deque
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def bfs(root):
            ret=[]
            # tmp=[]
            dq=deque([root])
            while dq:
                tmp=[]
                for i in range(len(dq)):
                    child=dq.popleft()
                    if child is not None:
                        tmp.append(child.val)
                        dq.append(child.left)
                        dq.append(child.right)
                    else:
                        tmp.append(None)

                if tmp is not None:
                    ret.append(tmp)
            return ret
        return bfs(p)==bfs(q)

# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#
#         queue1 = deque([p])
#         queue2 = deque([q])
#
#         while queue1 and queue2:
#             node1 = queue1.popleft()
#             node2 = queue2.popleft()
#             if node1.val != node2.val:
#                 return False
#             left1, right1 = node1.left, node1.right
#             left2, right2 = node2.left, node2.right
#             if (not left1) ^ (not left2):
#                 return False
#             if (not right1) ^ (not right2):
#                 return False
#             if left1:
#                 queue1.append(left1)
#             if right1:
#                 queue1.append(right1)
#             if left2:
#                 queue2.append(left2)
#             if right2:
#                 queue2.append(right2)
#
#         return not queue1 and not queue2

a=Solution()
print(a.isSameTree(p,q))