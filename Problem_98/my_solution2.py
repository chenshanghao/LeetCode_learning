# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            root_left, root_right = True, True
            if root.left:
                root_left = self.isVaildRange(root.left, float('-inf'), root.val)
            if root.right:
                root_right = self.isVaildRange(root.right, root.val, float('inf'))
        return (root_right and root_left)

    def isVaildRange(self, root, lmax, rmax):
        if root.val > lmax and root.val < rmax:
            node_left, node_right = True, True
            if root.left:
                node_left = self.isVaildRange(root.left, lmax, root.val)
            if root.right:
                node_right = self.isVaildRange(root.right, root.val, rmax)
            return (node_left and node_right)
        else:
            return False
                