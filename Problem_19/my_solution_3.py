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
        prev = ListNode(0)
        prev.next = head
        del_node = prev
        
        for i in range(n):
            del_node = del_node.next
            
        while(del_node.next):
            del_node = del_node.next
            prev = prev.next
            
        if prev.next == head:
            return head.next
        else:
            prev.next = prev.next.next
            return head