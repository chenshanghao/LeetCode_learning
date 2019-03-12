
def qsort(arr): 
     if len(arr) <= 1:
          return arr
     else:
          return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])


# LinkedList Initialization
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow, fast = head, head
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        # find the latter half of the linkedlist
        slow = slow.next
        slow = self.reverseLinkedList2(slow)
        
        while(slow):
            if head.val != slow.val:
                return False
            head = head.next 
            slow = slow.next
        return True
        
    def reverseLinkedList(self, head):
        new_head = None
        while(head):
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head
        
    def reverseLinkedList2(self, head):
        if not head or not head.next:
            return head
        p = self.reverseLinkedList2(head.next)
        head.next.next = head
        head.next = None
        return p




# TreeNode Initialization
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Preorder 先序遍历   根->左->右
# Postorder 后遍历   左->右->根
# Inorder 中序遍历   左->根->右
# Definition for a binary tree node.
class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        stack = []
        curr = root
        
        while(curr or stack):
            while(curr):
                stack.append(curr)
                curr = curr.left
                
            if stack:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
        
        return res

# recursively
def inorderTraversal1(self, root):
    res = []
    self.helper(root, res)
    return res
    
def helper(self, root, res):
    if root:
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)

# Construct Binary Tree from Preorder and Inorder Traversal
class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        inorder_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:inorder_index+1], inorder[0: inorder_index])
        root.right = self.buildTree(preorder[inorder_index+1:], inorder[inorder_index+1:])
        return root


# Validation Binary Tree
class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        
        return self._isValidBST(root.left, float('-inf'), root.val) and self._isValidBST(root.right, root.val, float('inf'))
    
    def _isValidBST(self, root, left_min, right_max):
        if not root:
            return True
        if not(root.val > left_min and root.val < right_max):
            return False
        return self._isValidBST(root.left, left_min,root.val) and self._isValidBST(root.right, root.val, right_max)





# binary Search
class Solution:
    def firstBadVersion(self, n):
        low, high = 1, n
        while(low < high):
            mid = (low+high)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low

def binary_search(arr,start,end,hkey):
    if start > end:
        return -1
    mid = start + (end - start) // 2
    if arr[mid] > hkey:
        return binary_search(arr, start, mid - 1, hkey)
    if arr[mid] < hkey:
        return binary_search(arr, mid + 1, end, hkey)
    return mid