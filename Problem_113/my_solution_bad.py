# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.result = []
        if not root:
            return self.result
        new_sum = sum - root.val
        
        path = [root.val]
        if (not root.left) and (not root.right ) and new_sum == 0:
            self.result.append(path)
            return self.result
        else: 
            if root.left is not None:
                left_path = path[:]
                left_path.append(root.left.val)
                self.findpathSum(root.left, new_sum, left_path)
            if root.right is not None:
                right_path = path[:]
                right_path.append(root.right.val)
                self.findpathSum(root.right, new_sum,right_path)
        
        return self.result
        
    def findpathSum(self, root, sum, path):
        new_sum = sum - root.val

        if new_sum == 0 and (not root.left) and (not root.right):
            self.result.append(path)
            return
        else:
            if root.left is not None:
                new_left_path = path[:]
                new_left_path.append(root.left.val)
                self.findpathSum(root.left, new_sum, new_left_path)
                
            if root.right is not None:
                new_right_path = path[:]
                new_right_path.append(root.right.val)
                self.findpathSum(root.right, new_sum, new_right_path)
            
        