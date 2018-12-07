# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        val = head.val
        temp = head
        while(temp.next != None):
            if val == temp.next.val:
                temp.next = temp.next.next
            else:
                val = temp.next.val
                temp = temp.next
        return head
            
            