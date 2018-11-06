# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        stack = [root]
        len_stack = len(stack)
        while(len_stack > 0):
            new_stack = []
            for index, node in enumerate(stack):
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
                if index < (len_stack-1):
                    node.next = stack[index+1]
            stack = new_stack
            len_stack = len(stack)