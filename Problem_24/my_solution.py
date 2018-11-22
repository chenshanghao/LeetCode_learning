# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None or head.next is None):
            return head
        
        pre_head = ListNode(0)
        pre_head.next = head
        L1, L2 = pre_head, head
        while(L2 and L2.next):
            temp_node = L2.next.next
            L1.next = L2.next
            L1.next.next = L2
            L2.next = temp_node
            L1 = L1.next.next
            L2 = L2.next
        
        return pre_head.next
            
            
            
        