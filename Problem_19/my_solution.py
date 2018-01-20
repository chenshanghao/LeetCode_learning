# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        prev, post = ListNode(0), ListNode(0)
        prev.next = head
        
        
        post = prev
        while(n > 0):
            post = post.next
            n -= 1
        while(post.next != None):
            prev = prev.next
            post = post.next
            
        if prev.next == head:
            return head.next
        else:
            prev.next = prev.next.next
            return head