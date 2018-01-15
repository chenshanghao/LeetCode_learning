# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}

    # iteratively
    def reverseList1(self, head):
        dummy = ListNode(0)

        while(head):
            next_node = head.next:
            head.next = dummy.next
            dummy.next = head
            head = next_node

        return  dummy.next

    # recursiverly
    def reverseList2(self, head):
        return self.doReverse(head None)
    def doReverse(self, head, newHead):
        if head is None:
            return newHead
        next = head.next
        head.next = newHead
        return self.doReverse(next, head)


