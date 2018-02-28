# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is not None:
            self.inOrder(root, result)
        return result
    
    def inOrder(self, root, result):
        if root.left is not None:
            self.inOrder(root.left, result)
        result.append(root.val)
        if root.right is not None:
            self.inOrder(root.right, result)
        
        
        