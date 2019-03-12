# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # dfs
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        # 分别以不同节点为根节点遍历
        return self.path(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    
    
    def path(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        num = 0
        if root:
            if root.val == sum:
                num += 1
            num += self.path(root.left, sum - root.val)
            num += self.path(root.right, sum - root.val)
        return num