# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        
        return self._isValidBST(root.left, float('-inf'), root.val) and self._isValidBST(root.right, root.val, float('inf'))
    
    def _isValidBST(self, root, left_min, right_max):
        if not root:
            return True
        if not(root.val > left_min and root.val < right_max):
            return False
        return self._isValidBST(root.left, left_min,root.val) and self._isValidBST(root.right, root.val, right_max)
        
            
        