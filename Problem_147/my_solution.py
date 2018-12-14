# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dump = ListNode(0)
        dump.next = head
        cur = head.next
        head.next = None
        while(cur):
            temp = cur
            cur = cur.next
            temp.next = None
            
            left,right = dump, dump.next
            while(right!=None and right.val<temp.val):
                right = right.next
                left = left.next
            if right == None:
                left.next = temp
            else:
                temp.next = right
                left.next = temp
        return dump.next
                
            
            
        