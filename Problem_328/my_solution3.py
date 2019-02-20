# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: 'ListNode') -> 'ListNode':
        # if not head or not head.next:
        #     return head
        
        dummy_odd= odd = ListNode(0)
        dummy_even= even = ListNode(0)
        
        flag = 1
        while(head):
            temp = head
            head = head.next
            temp.next = None
            if flag % 2 == 1:
                odd.next = temp
                odd = odd.next
            else:
                even.next = temp
                even = even.next
            flag+=1
        odd.next = dummy_even.next
        return dummy_odd.next
                
        
        
        