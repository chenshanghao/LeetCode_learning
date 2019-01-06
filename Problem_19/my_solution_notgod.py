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
        length = 0
        i = head
        
        while(i):
            length += 1
            i = i.next
        m = length - n + 1
        
        if m == 1:
            return head.next
        
        i, j=head, head.next
       
        while(m-2>0):
            i = i.next
            j = j.next
            m -= 1

        if j.next:
            j.val = j.next.val
            j.next = j.next.next
        else:
            i.next = None
        return head
        
        