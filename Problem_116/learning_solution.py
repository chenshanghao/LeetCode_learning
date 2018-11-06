class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return 
        while root.left:
            level=root.left
            cur=None
            while root:
                root.left.next=root.right
                cur=root.right
                root=root.next
                if cur and root:
                    cur.next=root.left
            root=level