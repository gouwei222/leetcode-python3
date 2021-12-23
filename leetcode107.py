# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if root is None:
            return []
        ret=[]
        queue=[root]
        while queue:
            tmp=[]
            ret.append([node.val for node in queue])
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue=tmp
        return ret[::-1]