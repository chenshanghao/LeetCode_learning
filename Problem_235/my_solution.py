# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        left_list = self.helper(root, p, [root])
        right_list = self.helper(root, q, [root])
        lst3 = [value for value in left_list if value in right_list] 
        return lst3[-1]
        
        
    def helper(self, root, node, res):
        if root == node:
            return res
        if root.left:
            left_res = res[::]
            left_res.append(root.left)
            left_list = self.helper(root.left, node, left_res)
            if  left_list:
                return left_list
        if root.right:
            right_res = res[::]
            right_res.append(root.right)
            right_list = self.helper(root.right, node, right_res)
            if  right_list:
                return right_list  
        return None
        
        