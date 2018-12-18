class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        for __ in range(m-1):
            node = node.next
        prev = node.next
        curr = prev.next
        for __ in range(n-m):
            next = curr.next
            curr.next = prev
            prev = curr
            curr =next
        node.next.next = curr
        node.next = prev
        return dummy.next
            
        
        
        
        
        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        prev = head
        curr = prev.next
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head.next = None
        return prev

            