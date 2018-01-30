# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        stack = [root]
        while(stack):
            temp_value_array, temp_node_array = [], []
            while(stack):
                a = stack.pop(0)
                temp_value_array.append(a.val)
                if a.left:
                    temp_node_array.append(a.left)
                if a.right:
                    temp_node_array.append(a.right)
            result.append(temp_value_array)
            stack = temp_node_array
        return result
            