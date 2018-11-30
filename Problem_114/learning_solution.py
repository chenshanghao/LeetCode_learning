# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        # 1. in-place 不能额外空间
        # step 1: 右 -> 左leaf
        # step 2: 左替代右
        # step 3: 左 = None
        
        if not root:
            return None
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        # no left sub tree
        if root.left == None:
            return None
        
        #下面的已经flatten
        node = root.left
        while node.right != None:
            node = node.right
            
        node.right = root.right
        root.right = root.left
        root.left = None
        
        return
        
        