# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        new_head1, new_head2 = ListNode(0), ListNode(0)
        cur_1, cur_2 = new_head1, new_head2
        while(head!=None):
            temp = head.val
            if temp < x:
                cur_1.next = ListNode(temp)
                cur_1 = cur_1.next
            else:
                cur_2.next = ListNode(temp)
                cur_2 = cur_2.next
            head = head.next
        cur_1.next = new_head2.next
        return new_head1.next