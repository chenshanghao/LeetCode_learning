# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        if abs(right_depth - left_depth) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getDepth(self, root):
        if not root:
            return 1
        else:
            return 1+ max(self.getDepth(root.left), self.getDepth(root.right))
    