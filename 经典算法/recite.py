
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


# TreeNode Initialization
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# reverse LinkedList
class Solution:
    def reverseLinkedList(self, head):
        if not head or not head.next:
            return head
        p = self.reverseLinkedList(head.next)
        head.next.next = head
        head.next = None
        return p


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