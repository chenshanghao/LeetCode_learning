# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        stack = [root]
        level = 1
        while stack:
            new_stack = []
            for node in stack:
                if node.left:   new_stack.append(node.left)
                if node.right:  new_stack.append(node.right)
            ans = [node.val for node in stack]
            if level%2==0:
                ans = ans[::-1]
            res.append(ans)
            stack = new_stack
            level+=1
        return res
        