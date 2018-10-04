# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        #attention:
        # 1. Given n will always be valid.


        prev = ListNode(0)
        tail = prev
        prev.next = head
        
        while(n > 0):
            tail = tail.next
            n -= 1
        while(tail.next != None):
            tail = tail.next
            prev = prev.next
            
        ### 至关重要
        if prev.next == head:
            return head.next
        else:
            prev.next = prev.next.next
            return head
        
        return head