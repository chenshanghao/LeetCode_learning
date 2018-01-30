# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p and q:
            if p.val == q.val:
                left_equal, right_equal = False, False
                # test_left tree
                if p.left and q.left:
                    left_equal = self.isSameTree(p.left, q.left)
                elif (p.left is None) and (q.left is None):
                    left_equal = True
                else:
                    left_equal = False
                # test_right tree
                if p.right and q.right:
                    right_equal = self.isSameTree(p.right, q.right)
                elif (p.right is None) and (q.right is None):
                    right_equal = True
                else:
                    right_equal = False    
                return (left_equal and right_equal)
            else:
                return False
        else:
            return False
            
            
        