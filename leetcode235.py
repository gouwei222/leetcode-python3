# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root

#我们从根节点开始遍历；

#如果当前节点的值大于 p和 q的值，说明 p和 q应该在当前节点的左子树，因此将当前节点移动到它的左子节点；

#如果当前节点的值小于 p 和 q的值，说明 p和 q应该在当前节点的右子树，因此将当前节点移动到它的右子节点；

#如果当前节点的值不满足上述两条要求，那么说明当前节点就是「分岔点」。此时，p和 q要么在当前节点的不同的子树中，要么其中一个就是当前节点。

