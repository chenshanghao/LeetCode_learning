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
        result = []
        if not root:
            return result
        stack = [root]
        node = None
        while (stack!=[]) or (node != None):
            if not node:
                node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            node = node.left
        return result
                
            
        