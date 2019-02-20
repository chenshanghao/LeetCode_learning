"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        stack = [root]
        while(stack):
            new_stack = []
            len_stack = len(stack)
            for index, node in enumerate(stack):
                if node.left:   new_stack.append(node.left)
                if node.right:  new_stack.append(node.right)
                if index < len_stack-1:
                    node.next = stack[index+1]
            stack = new_stack 
        return root