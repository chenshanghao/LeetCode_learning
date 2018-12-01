# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # Inorder (Left, Root, Right)   中序
        # Preorder (Root, Left, Right)  先序
        # Postorder (Left, Right, Root) 后序
        
        
        # 1. Why it root.right first?
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        inoder_root_index = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[:inoder_root_index], postorder[:inoder_root_index])
        root.right = self.buildTree(inorder[inoder_root_index+1:], postorder[inoder_root_index:-1])
        
        return root