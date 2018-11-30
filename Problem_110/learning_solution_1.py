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
        if self.dfs(root) == -1:
            return False
        else:
            return True
        
    def dfs(self, root):
        if not root:
            return 0
        left_depth, right_depth = self.dfs(root.left), self.dfs(root.right)
        
        if left_depth == -1:
            return -1
        if right_depth == -1:
            return -1
        if abs(left_depth - right_depth) > 1:
            return -1
        else:
            return 1+max(left_depth, right_depth)
        
        