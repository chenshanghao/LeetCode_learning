# Recursively    
def swapPairs(self, head):
    if head and head.next:
        tmp = head.next
        head.next = self.swapPairs(tmp.next)
        tmp.next = head
        return tmp
    return head

public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        
        ListNode swappedList = swapPairs(head.next.next);
        
        ListNode newHead = head.next;
        head.next.next = head;
        head.next = swappedList;
        
        return newHead;
        
        
    }