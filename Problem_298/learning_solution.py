"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    
    def longestConsecutive(self, root):
        # write your code here
        self.maxConsecutivePath = 0
        if not root:
            return self.maxConsecutivePath
            
        self.helper(root)
        return self.maxConsecutivePath
    
    def helper(self, root):
        if not root:
            return 0
        
        max_left = self.helper(root.left)
        max_right = self.helper(root.right)
        
        maxConsecutivePath = 1
        if root.left and root.val+1 == root.left.val:
            maxConsecutivePath = max(maxConsecutivePath, max_left+1)
        if root.right and root.val+1 == root.right.val:
            maxConsecutivePath = max(maxConsecutivePath, max_right+1)
        if maxConsecutivePath > self.maxConsecutivePath:
            self.maxConsecutivePath = maxConsecutivePath
        return maxConsecutivePath
        
