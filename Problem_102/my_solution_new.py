# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        temp = [root]
        
        while(temp):
            new_temp = []
            for node in temp:
                if node.left:
                    new_temp.append(node.left)
                if node.right:
                    new_temp.append(node.right)
            val_temp = [i.val for i in temp]
            ans.append(val_temp)
            temp = new_temp
        return ans