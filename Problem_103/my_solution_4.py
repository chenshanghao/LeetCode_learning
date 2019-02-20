# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []
        if not root:
            return res
        stack = [root]
        level = 1
        while(stack):
            new_stack = []
            value_list = []
            for node in stack:
                value_list.append(node.val)
                if node.left:   new_stack.append(node.left)
                if node.right:  new_stack.append(node.right)
            if level % 2 == 1:
                res.append(value_list)
            else:
                res.append(value_list[::-1])
            level += 1
            stack = new_stack
        return res
        