# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow = fast = head
        while(fast and fast.next):

            slow = slow.next
            fast = fast.next.next
        left = slow.next
        slow.next = None
        # print(slow.val, slow.next.val)
        # return
        left,right = head, self.reverseList(left)
        while(right):
            next_left, next_right = left.next, right.next
            left.next = right
            right.next = next_left
            left, right = next_left, next_right
    
    def reverseList(self, head):
        if not head or not head.next:
            return head
        pre = ListNode(0)
        pre.next = head
        
        curr = head
        head = head.next
        curr.next = None
        while(head):
            curr = head
            head=head.next
            curr.next = pre.next
            pre.next = curr
        return pre.next