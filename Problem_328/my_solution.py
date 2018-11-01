# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head
            
        pre_head = ListNode(0)
        pre_head.next = head
        odd_head, even_head = head, head.next
        ptr_odd, ptr_even =odd_head, even_head
        head = head.next.next
        flag = 1
        while(head):
            if flag == 1:
                odd_head.next = head
                odd_head = odd_head.next
            else:
                even_head.next = head
                even_head = even_head.next
            flag = abs(flag -1)
            head = head.next
        odd_head.next = ptr_even
        even_head.next = None
        pre_head.next = ptr_odd
        return ptr_odd
        
            
         
        
        
        