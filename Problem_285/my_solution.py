"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not p:
            return None
        if p.right:
            cur = p.right
            while(cur):
                if cur.left:
                    cur = cur.left
                else:
                    break
            return cur

        cur = root
        last_cur = None
        while(cur):
            if cur == p:
                return last_cur
            if cur.val > p.val:
                last_cur = cur
                cur = cur.left
            else:
                cur = cur.right
        return
    
