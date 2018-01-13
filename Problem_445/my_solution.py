# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_reverse = self.reverseList(l1)
        l2_reverse = self.reverseList(l2)
        return self.reverseList(self.addTwoNumbers2(l1_reverse, l2_reverse))
        
            
    def reverseList(self, head):
        dummp = ListNode(0)
        while(head):
            head_next = head.next
            head.next = dummp.next
            dummp.next = head
            head = head_next
        return dummp.next
    
    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode(0)
        ptr = head
        carry  = 0
        while True:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            ptr.val = carry % 10
            carry /= 10
            # 运算未结束新建一个节点用于储存答案，否则退出循环
            if l1 != None or l2 != None or carry != 0:
                ptr.next = ListNode(0)
                ptr = ptr.next
            else: 
                break
        return head