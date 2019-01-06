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
        len_A,len_B = 0,0
        temp = headA
        while(temp):
            len_A +=1
            temp = temp.next
        temp = headB
        while(temp):
            len_B += 1
            temp = temp.next
        
        poiter_a, poiter_b = headA, headB
        n = abs(len_A-len_B)
        if len_A > len_B:
            while(n>0):
                poiter_a = poiter_a.next
                n -= 1
        else:
            while(n>0):
                poiter_b = poiter_b.next
                n -= 1
        while(poiter_a):
            if poiter_a == poiter_b:
                return poiter_a
            else:
                poiter_a = poiter_a.next
                poiter_b = poiter_b.next
        return None