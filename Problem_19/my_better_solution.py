# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        prev = ListNode(0)
        tail = prev
        prev.next = head
        
        while(n>0):
            tail = tail.next
            n -=1
        while(tail.next):
            tail = tail.next
            prev = prev.next
        ### if delete the node is head
        if prev.next == head:
            return head.next
        else:
            prev.next = prev.next.next
            
        return head
            
        

        
        