# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        if not root:
            return self.res
        else:
            self.dfs(root, self.res, str(root.val))
        return self.res
    
    def dfs(self, node, res, temp):
        if not node.left and not node.right:
            res.append(temp)
            return
        if node.left:
            self.dfs(node.left, res, temp + '->' + str(node.left.val))
        if node.right:
            self.dfs(node.right, res, temp + '->' + str(node.right.val))