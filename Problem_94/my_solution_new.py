# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Inorder traversal
# Left -> Root -> Right
        
# Preorder traversal
# Root -> Left ->Right

# Postorder traversal
# Left ->Right -> Root

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        else:
            self.inorder(root, result) 
        return result
    
    def inorder(self, root, result):
        if root.left is not None:
            self.inorder(root.left, result)
        result.append(root.val)
      
        if root.right is not None:
            self.inorder(root.right, result)
