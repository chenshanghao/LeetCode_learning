# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.check(root.left, root.right)
        
    def check(self, l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.val != r.val:
            return False
        return self.check(l.left,r.right) and self.check(l.right,r.left)