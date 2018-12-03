# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = [root]
        res.append(root.val)
        while(stack != []):
            new_stack = []
            right = None
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                    right = node.left
                if node.right:
                    new_stack.append(node.right)
                    right = node.right
            if right:
                res.append(right.val)
            stack = new_stack
        return res
            