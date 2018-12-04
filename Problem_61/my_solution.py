# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        len_list = 0
        value_list = []
        l = head
        while(l):
            value_list.append(l.val)
            len_list += 1
            l = l.next
        if len_list <=1:
            return head
        k = k % len_list
        
        for i in range(len_list-1, len_list-1-k, -1):
            curr = ListNode(value_list[i])
            curr.next = head
            head = curr
        curr = head
        for i in range(len_list-1):
            curr = curr.next
        curr.next = None
        return head
            
        
        