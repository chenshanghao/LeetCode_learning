# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #empty
        if root is None:
            return True
        if not (root.left or root.right):
            return True
        return self.Smyetric(root.left, root.right)
        
    def Smyetric(self, left_node, right_node):
        if not (left_node or right_node):
            return True
        elif left_node and right_node:
            if left_node.val == right_node.val:
                return self.Smyetric(left_node.right, right_node.left) and self.Smyetric(left_node.left, right_node.right)
            else:
                return False
        else:
            return False
        