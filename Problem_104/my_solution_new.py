# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        if root.left:
            max_left_depth = self.maxDepth(root.left)
        else:
            max_left_depth = 0
            
        if root.right:
            max_right_depth = self.maxDepth(root.right)
        else:
            max_right_depth = 0
        return max(max_left_depth, max_right_depth) + 1
            
        