# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.BST_test(root, float('-inf'), float('inf'))
    
    def BST_test(self, root, left, right):
        if not root:
            return True
        
        if root.val > left and root.val < right:
            left_test = self.BST_test(root.left, left, root.val)
            right_test = self.BST_test(root.right, root.val,right)
            return left_test and right_test
            
        else:
            return False
        