from binarytree import *
from collections import *
root=Node(3)
root.left=Node(9)
root.right=Node(20)
root.right.left=Node(15)
root.right.right=Node(7)
# p.right.left=Node(4)
print(root)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:##找到一个p或q
            return root
        if root is None:
            return root
        left=self.lowestCommonAncestor(root.left,p,q) #左子树中pq的公共祖先，找到与p或者q相等的作为root，找另一个p或q
        right=self.lowestCommonAncestor(root.right,p,q)#右子树中pq的公共祖先，找到与p或者q相等的作为root
        if not left and not right:#p或q不在当前为根的树里
            return None
        if right and not left:#p,q在当前节点的右子树
            return right
        if left and not right:#p,q在当前节点的左子树
            return left
        if left and right:#刚好在当前节点root的左右两边
            return root
#p跟q一定在这个树里面，从上往下递归，先找到了p，那么q要么在p的子树里面，要么在根root的另外半个子树里
#所有结点都不同，左边找到p，则右边找到的一定是q,反之亦然
#分四种情况，1.root是null或者root等于p或q，说明root是p，q的公共祖先，2.递归左右子树，如果左右子树递归函数返回的都不为空，则root就是p，q的公共祖先，
# 3.左子树递归函数返回的值为空，则p，q都在右子树，4.右子树递归函数返回的值为空，则p，q都在左子树




a=Solution()
p,q=Node(9),Node(20)
print(a.lowestCommonAncestor(root,p,q))