"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given tree
    @return: the number of uni-value subtrees.
    """
    def countUnivalSubtrees(self, root):
        # write your code here
        self.res = 0
        if not root:
            return self.res
        self.helper(root)
        return self.res
        
        
    def helper(self, node):
        if not node:
            return True
        if not node.left and not node.right:
            self.res += 1
            return True
        
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        if not left or not right:
            return False
        if not node.left and node.val == node.right.val:
            self.res += 1
            return True
        if not node.right and node.val == node.left.val:
            self.res += 1
            return True
        if node.left and node.right and node.left.val == node.right.val  and node.val == node.left.val:
            self.res += 1
            return True
        return False
        
        