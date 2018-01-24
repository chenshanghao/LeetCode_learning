# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isValidRightBST(root) and self.isValidLeftBST(root)

        
        
    def isValidRightBST(self, root):
        if root.right is None:
            return True
        elif root.right.val > root.val:
            return self.isValidBST(root.right) 
        else:
            return False
        
    def isValidLeftBST(self, root):
        if root.left is None:
            return True
        elif root.left.val < root.val:
            return self.isValidBST(root.left) 
        else:
            return False