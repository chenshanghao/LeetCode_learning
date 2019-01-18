# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.list = []
        self.cur = 0
        if not root:
            self.length = 0
        else:
            self.preorder(root)
            self.length = len(self.list)
        
        
    def preorder(self, root):
        if root.left:   self.preorder(root.left)
        self.list.append(root.val)
        if root.right:  self.preorder(root.right)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.cur < self.length:
            self.cur += 1
            return self.list[self.cur-1]
        else:
            return None
        
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return True if self.cur < self.length else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()