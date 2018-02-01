# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA, lenB = 0, 0
        node_A, node_B = headA, headB
        while(node_A):
            lenA += 1
            node_A = node_A.next
        while(node_B):
            lenB += 1
            node_B = node_B.next
        
        node_A, node_B = headA, headB
        while lenA > lenB:
            node_A = node_A.next
            lenA -= 1
        
        while lenB > lenA:
            node_B = node_B.next
            lenB -= 1
        while node_A != node_B:   #Null结点最终会相等
            node_A = node_A.next
            node_B = node_B.next
            
        return node_A
        