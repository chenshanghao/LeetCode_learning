# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        if (not root.left) and (not root.right) and (root.val == sum):
            return True
        elif (not root.left) and (not root.right) and (root.val != sum):
            return False
        left_flag, right_flag =False, False
        if root.left != None:
            left_flag = self.hasPathSum(root.left, sum - root.val) 
        if root.right != None:
            right_flag = self.hasPathSum(root.right, sum - root.val)
        return (left_flag or right_flag)