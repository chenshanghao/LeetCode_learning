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
        if not l1:
            return l2
        elif not l2:
            return l1
        
        pre_header = ListNode(0)
        ptr = pre_header
        carry = 0
        while(True):
            sum_value = 0
            if l1:
                sum_value += l1.val
                l1 = l1.next
            if l2:
                sum_value += l2.val
                l2 = l2.next
            sum_value += carry
            ptr.val = sum_value % 10
            carry = sum_value // 10
            
            if (not l1) and (not l2) and carry == 0:
                break
            ptr.next = ListNode(0)
            ptr = ptr.next
                
        return pre_header        