# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # empty or one element
        if not head or not head.next:
            return True
        
        # find the midpoint
        slow = fast = head
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        
        slow = slow.next
        slow = self.reverseLinkedList(slow)
        
        while slow:
            if head.val != slow.val:
                return False
            else:
                slow = slow.next
                head = head.next
        
    def reverseLinkedList(self, head):
        if not head or not head.next:
            return head
        p =self.reverseLinkedList(head)
        head.next.next = head
        head.next = None
        return p
        
        