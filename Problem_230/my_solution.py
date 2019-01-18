# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res = []
        if not root:
            return None
        self.inOrder(root)
        return self.res[k-1]
        
    def inOrder(self, root):
        if root.left:
            self.inOrder(root.left)
        self.res.append(root.val)
        if root.right:
            self.inOrder(root.right)