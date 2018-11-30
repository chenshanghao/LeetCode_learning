# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.getDepth(root)
        return self.checkisBalance(root)
    
    def checkisBalance(self, root):
        if not root:
            return True
        
        left_depth = root.left.val if root.left else 0
        right_depth = root.right.val if root.right else 0
        if abs(left_depth -right_depth) > 1:
            return False
        else:
            
            return self.checkisBalance(root.left) and self.checkisBalance(root.right)
        
    def getDepth(self, root):
        if root == None:
            return 0
        root.val = 1 + max(self.getDepth(root.left), self.getDepth(root.right))
        return root.val
