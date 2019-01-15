# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        curr = [root]
        level = 1
        while curr:
            next_curr = []
            ans = []
            for node in curr:
                ans.append(node.val)
                if node.left:
                    next_curr.append(node.left)
                if node.right:
                    next_curr.append(node.right)
            if level % 2 == 1:
                res.append(ans)
            else:
                res.append(ans[::-1])
            level+=1
            curr = next_curr
        return res
        