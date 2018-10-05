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
        if not root:
            return True
        else:
            right, left = True, True
            if root.left:
                left = self.isValidNode(root.left, float('-inf'),root.val) 
                
            if root.right:
                right = self.isValidNode(root.right,root.val, float('inf'))
                
            return left and right
            
        
    def isValidNode(self, root, min_v, max_v):
        if root.val > min_v and root.val < max_v:
            right_flag, left_flag = True, True
            if root.left:
                left_flag = self.isValidNode(root.left, min_v, root.val)
            if root.right:
                right_flag =  self.isValidNode(root.right, root.val, max_v)
            return  left_flag and right_flag
        else:
            return False
        
        