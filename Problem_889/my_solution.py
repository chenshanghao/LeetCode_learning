# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if (not pre) or (not post):
            return None
        root = TreeNode(pre[0])
        if len(pre) > 1:
            left_index = post.index(pre[1])
            root.left = self.constructFromPrePost(pre[1:left_index+2], post[:left_index+1])
            root.right = self.constructFromPrePost(pre[left_index+2:],post[left_index+1:-1])
        else:
            root.left = None
            root.right = None

        return root