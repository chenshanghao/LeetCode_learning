# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        if not root:
            return self.res
        self.dfs(root,  '')
        return self.res
        
    def dfs(self, node, path):
        if not node.left and not node.right:
            self.res += int(path + str(node.val))
            return
        if node.left:
            self.dfs(node.left,path + str(node.val))
        if node.right:
            self.dfs(node.right, path + str(node.val))
            
        
        