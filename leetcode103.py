from binarytree import *
p=Node(3)
p.left=Node(9)
p.right=Node(20)
p.right.left=Node(15)
p.right.right=Node(7)
# p.right.left=Node(4)
print(p)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) :
        if root is None:
            return []
        res=[]
        i=0
        queue=[root]
        while(queue):
            tmp=[]
            ret=([node.val for node in queue])#####ret只存每一层的val
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue=tmp
            if (i%2)==0:
                res.append(ret)
            else:
                res.append(ret[::-1])
            i+=1
        return res
a=Solution()
print(a.zigzagLevelOrder(p))