# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        node = root
        
        # find the minimum in 栈顶
        while node:
            stack.append(node)
            node = node.left
        x = 1
        while stack and x<=k:
            n = stack.pop()
            x += 1
            
            w = n.right
            while w:
                stack.append(w)
                w = w.left
        return n.val
        
            