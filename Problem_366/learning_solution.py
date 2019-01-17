"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        self.res = []
        self.helper(root, self.res)
        return self.res
    
    def helper(self, node, res):
        if not node:
            return -1
        
        lenth = 1 + max(self.helper(node.left, res), self.helper(node.right, res))
        if len(res) <= lenth:
            res.append([])
        res[lenth].append(node.val)
        return lenth
            
        
        
    
    