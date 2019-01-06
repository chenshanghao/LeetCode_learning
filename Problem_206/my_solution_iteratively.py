# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        
        # if it is empty linked list
        if not head:
            return head
        
        i,j = head, head.next
        i.next = None
        
        while(j):
            pre.next = j
            j = j.next
            pre.next.next = i
            i = pre.next
        return pre.next
            
        