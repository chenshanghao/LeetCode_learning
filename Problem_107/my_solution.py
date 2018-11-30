# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.result = []
        if not root:
            return self.result
        stack = [root]
        new_stack = []
        while(stack != []):
            new_list = []
            for node in stack:
                new_list.append(node.val)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            self.result.append(new_list)
            stack=new_stack
            new_stack =[]
        return self.result[::-1]
        