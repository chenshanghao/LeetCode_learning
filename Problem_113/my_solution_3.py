# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        if not root:
            return self.res
        self.dfs(root, sum, self.res,[root.val])
        return self.res
    
    def dfs(self, node, sum_val, res, path):
        if not node.left and not node.right and sum(path) == sum_val:
            res.append(path)
        if node.left:
            left_path = path[::]
            left_path.append(node.left.val)
            self.dfs(node.left, sum_val, res, left_path)
            
        if node.right :
            right_path = path[::]
            right_path.append(node.right.val)
            self.dfs(node.right, sum_val, res, right_path)
            