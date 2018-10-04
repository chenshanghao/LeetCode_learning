# Iterative

# 1. need extra storage space
class Solution:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


# 2. my+soultion
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None :
            return head
        prev, post = head, head
        while(post.next != None):
            new_head = post.next
            post.next = post.next.next
            new_head.next = prev
            prev = new_head
        return prev

# Recursively  (https://www.youtube.com/watch?v=MRe3UsRadKw)
# 1. Start with node curr as head
# 2. If curr's next element is null, this means it is the last node, so make this as head
# because the last node will be the head of reversed list. Return
# 3. Recursively traverse the list.
# 4. Set curr->next-next to curr.
# 5. Set curr->next to null


class Solution(object):
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)