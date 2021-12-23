#从前序与中序遍历中构建二叉树
from binarytree import *
p=Node(3)
p.left=Node(9)
p.right=Node(20)
p.right.left=Node(15)
p.right.right=Node(7)
# p.right.left=Node(4)
# print(p)




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder or not inorder:
            return None
        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:mid+1],inorder[0:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
a=Solution()
print(a.buildTree([3,9,20,15,7],[9,3,15,20,7]))