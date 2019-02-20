# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []
        if not root:
            return res
        temp = [root]
        while(temp!=[]):
            new_temp = []
            new_res = []
            for node in temp:
                new_res.append(node.val)
                if node.left:   
                    new_temp.append(node.left)
                if node.right:  
                    new_temp.append(node.right)
            res.append(new_res)
            temp = new_temp[:]
        return res