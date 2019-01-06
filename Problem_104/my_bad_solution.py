# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0 
        return self.getDepth(root, 1)
    
    def getDepth(self, node, depth):
        depth, left_length, right_length = depth, 0, 0
        if node.left:
            left_length = self.getDepth(node.left, depth+1)
        if node.right:
            right_length = self.getDepth(node.right, depth+1) 
        return max(depth,left_length, right_length)
        