# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        linklist = []
        while(head):
            linklist.append(head.val)
            head = head.next
        
        len_linklist = len(linklist)
        if len_linklist == 0:
            return None
        
        return self.buldBST(linklist)
        
    def buldBST(self,linklist):
        len_linklist = len(linklist)
        mid = len_linklist //2
        root = TreeNode(linklist[mid])
        if len(linklist[0:mid]) > 0:     
            root.left = self.buldBST(linklist[0:mid])
        else:
            root.left = None
        if len(linklist[mid+1:]) > 0:
            root.right = self.buldBST(linklist[mid+1:])
        else:
            root.right = None
        return root