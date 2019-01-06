# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        odd_head, even_head = head, head.next
        head = head.next.next
        odd_head.next= None
        even_head.next = None
        temp_odd, temp_even = odd_head, even_head
        
        while(head and head.next):
            temp_odd.next = head
            head = head.next
            temp_odd = temp_odd.next 
            temp_odd.next = None
            
            temp_even.next = head
            head = head.next
            temp_even = temp_even.next
            temp_even.next = None
        
        if head:
            temp_odd.next = head
            temp_odd = temp_odd.next
            temp_odd.next = None
        
        temp_odd.next = even_head
        return odd_head
        
            
        
            
            
        