# Definition for a binary tree node.
from collections import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ret=[]
        queue=deque([root])
        while queue:
            tmp=[]
            ret.append([node.val for node in queue][-1])
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue=tmp
        return ret