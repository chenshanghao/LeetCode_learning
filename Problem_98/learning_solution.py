# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
######################
#于这棵树而言，怎样进行递归呢？root.left这棵树的所有节点值都小于root，
#root.right这棵树的所有节点值都大于root。然后依次递归下去就可以了。
#例如：如果这棵树是二叉查找树，那么左子树的节点值一定处于（负无穷，4）这个范围内，
#右子树的节点值一定处于（4，正无穷）这个范围内。思路到这一步，程序就不难写了。
class Solution:
    # @param root, a tree node
    # @return a boolean
    def ValidBST(self, root, min, max):
        if root == None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.ValidBST(root.left, min, root.val) and self.ValidBST(root.right, root.val, max)
    
    def isValidBST(self, root):
        return self.ValidBST(root, -2147483648, 2147483647)