# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.finLeaf(root, 1)
        
    def finLeaf(self, root, depth):
        if (not root.left) and (not root.right):
            return depth
        left_min, right_min = float('inf'), float('inf')
        
        if (root.left):
            left_min = self.finLeaf(root.left, depth+1)
            
        if (root.right):
            right_min =self.finLeaf(root.right, depth+1)
        return min(left_min, right_min)
            