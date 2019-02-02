"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque
from collections import defaultdict

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        # write your code here
        res = []
        if not root:
            return res
        
        dic_Pos_List = defaultdict(list)
        leftMost, rightMost = 0, 0
        queue = deque()
        queue.append((root, 0))
        
        while queue:
            node, pos = queue.popleft()
            dic_Pos_List[pos].append(node.val)
            
            if node.left:
                queue.append((node.left, pos-1))
                leftMost = min(leftMost, pos-1)
            if node.right:
                queue.append((node.right, pos+1))
                rightMost = max(rightMost, pos+1)
                
        for pos in range(leftMost, rightMost+1):
            res.append(dic_Pos_List[pos])
        return res
            
        
        