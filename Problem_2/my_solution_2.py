# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        head = ListNode(-1)
        temp = head
        carry = 0
        while(l1 or l2):
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            carry = sum_val // 10
            temp.next = ListNode(sum_val%10)
            temp = temp.next
        
        if carry != 0:
            temp.next = ListNode(carry)
        
        return head.next
            
            