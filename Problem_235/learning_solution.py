# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
# 根据二叉搜索树的性质，对于树中从root开始的节点： 
# 如果p和q的值如果都小于root的值，那么它们的最低公共祖先一定在root的左子树；如果p和q的值如果都大于root的值，那么它们的最低 公共祖先一定在root的右子树；其他情况则说明最低公共祖先就是root节点。如此循环判断即可

        if not root:
            return None
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        