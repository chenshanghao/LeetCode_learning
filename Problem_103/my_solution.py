# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is None:
            return result
        count = 0
        stack = [root]
        while(stack != []):
            new_stack = []
            for node in stack:
                if node.left is not None:
                    new_stack.append(node.left)
                if node.right is not None:
                    new_stack.append(node.right)
            value_list = []
            for node in stack:
                value_list.append(node.val)
            if count%2 == 1:
                value_list = value_list[::-1]
            result.append(value_list)
            stack = new_stack
            count += 1
        return result
                
                
            
        
        