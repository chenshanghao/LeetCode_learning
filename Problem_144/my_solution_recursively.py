# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        if not root:
            return self.result
        else:
            self.preTrave(root, self.result)
        return self.result
        
    
    def preTrave(self, root, result):
        result.append(root.val)
        if root.left:
            self.preTrave(root.left, result)
        if root.right:
            self.preTrave(root.right, result)
        