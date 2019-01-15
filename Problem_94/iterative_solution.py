# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                # Save the nodes which have left child
                stack.append(curr)
                curr = curr.left
            if stack:
                curr = stack.pop()
                # Visit the middle node
                res.append(curr.val)
                # Visit the right subtree
                curr = curr.right
        return res
        
        
        
        