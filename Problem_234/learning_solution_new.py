# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 空 或者 1个元素
        if not head or not head.next:
            return True
        
        # 快慢指针找重点
        slow = fast = head
        while(fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
           
        # slow指向链表的后半段
        slow = slow.next
        slow = self.reverseList(slow)
        
        while(slow):
            if head.val != slow.val:
                return False
            else:
                slow = slow.next
                head = head.next
        return True
        
    def reverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head
        
            
            
        