# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # Edge condition:
        if not root:
            return True
        
        # Process:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            else:
                return dfs(left.left, right.right) and dfs(left.right, right.left)
    
        
        # Recursion
        return dfs(root.left, root.right)
        