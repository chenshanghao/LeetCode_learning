# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow, fast = head, head
        while(True):
            if (fast.next == None) or (fast.next.next == None):
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        slow = head

        while(slow != fast):
            slow = slow.next
            fast = fast.next     
        return slow
        