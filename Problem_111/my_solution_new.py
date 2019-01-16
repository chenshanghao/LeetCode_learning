# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.minpath = float('inf')
        self.helper(root,1)
        return self.minpath
        
    def helper(self, node, path):
        if not node.left and not node.right:
            self.minpath =  min(self.minpath, path)
            return
        if node.left and path < self.minpath:
            self.helper(node.left, path+1)
        if node.right and path < self.minpath:
            self.helper(node.right, path+1)
        