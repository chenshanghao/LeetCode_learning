# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, start, end):
        # if start > end:
        #     return [None]
        if start > end:
            return [None]
        res = []
        for curr_root in range(start, end+1):
            left = self.helper(start, curr_root -1)
            right = self.helper(curr_root+1, end)
            
            for l in left:
                for r in right:
                    root = TreeNode(curr_root)
                    root.left =l
                    root.right = r
                    res.append(root)
        return res
        
        
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.helper(1, n)
    
        