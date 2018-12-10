# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = 0
        self.path_list = []
        if not root:
            return ret
        self.dfs(root,[root.val])
        for path in self.path_list:
            temp = 0
            for value in path:
                temp = temp*10 +value 
            ret += temp
        return ret
        
    def dfs(self, node, path):
        if node.left == None and node.right == None:
            self.path_list.append(path)
        if node.left != None:
            left_path = path[:]
            left_path.append(node.left.val)
            self.dfs(node.left, left_path)
        if node.right != None:
            right_path = path[:]
            right_path.append(node.right.val)
            self.dfs(node.right, right_path)
            