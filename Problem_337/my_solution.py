# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.helper(root))
        
        
    def helper(self, root):
        if not root:
            return (0, 0)
        left, left_not = self.helper(root.left)
        right, right_not = self.helper(root.right)
        
        return ((left_not + right_not + root.val), max(left + right, left_not+right, left+right_not, left_not + right_not))