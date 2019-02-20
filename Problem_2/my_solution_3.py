# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if not l1 or not l2:
            return l1 or l2
        dummy = ListNode(-1)
        tail = dummy
        carry = 0
        while(l1 or l2):
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            tail.next = ListNode(sum_val % 10)
            tail = tail.next
            carry = sum_val //10
        if carry != 0:
            tail.next = ListNode(carry)
            tail.next.next = None
        else:
            tail.next = None
        return dummy.next
        