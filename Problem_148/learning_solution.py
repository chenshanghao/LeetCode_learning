# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        slow = fast = head
        while(fast and fast.next):
            pre=slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return self.merge(self.sortList(head), self.sortList(slow))
    
    def merge(self, left, right):
        res = cur = ListNode(0)
        while(left and right):
            if left.val < right.val:
                cur.next = left
                cur = cur.next
                left = left.next
            else:
                cur.next = right
                cur = cur.next
                right = right.next
        if left: cur.next = left
        if right: cur.next =right
        return res.next
        