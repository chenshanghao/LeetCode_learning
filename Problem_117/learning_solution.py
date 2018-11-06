def connect(self, node):
    tail = dummy = TreeLinkNode(0)
    while node:
        tail.next = node.left
        if tail.next:
            tail = tail.next
        tail.next = node.right
        if tail.next:
            tail = tail.next
        node = node.next
        if not node:
            tail = dummy
            node = dummy.next