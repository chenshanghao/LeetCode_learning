# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathSum = float('-inf')
        self._maxPathSum(root)
        return self.maxPathSum
    
    def _maxPathSum(self, node):
        if not node:
            return 0
        left = self._maxPathSum(node.left)
        right = self._maxPathSum(node.right)
        
        left = left if left > 0 else 0
        right = right if right > 0 else 0
        self.maxPathSum = max(self.maxPathSum, node.val + left + right)
        return max(left, right) + node.val
        
        