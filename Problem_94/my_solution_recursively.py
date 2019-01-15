# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        self.inorderTraver(root, res)
        return res
    
    def inorderTraver(self, root, res):
        if root.left:
            self.inorderTraver(root.left, res)
        res.append(root.val)
        if root.right:
            self.inorderTraver(root.right, res)
        
        
        