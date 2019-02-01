"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        self.node_list = self.inorderTraversal(root)
        
        n = len(self.node_list)
        

        pos, min_dis = -1, float('inf')
        for i in range(n):
            if abs(self.node_list[i].val - target) < min_dis:
                min_dis = abs(self.node_list[i].val - target)
                pos = i
        
        ans_list = [self.node_list[pos].val]
        left = pos-1 if pos>=1 else -1
        right = pos+1 if pos<(n-1) else -1
        
        while(k > 1):
            left_node_dis = abs(self.node_list[left].val - target) if left!=-1 else float('inf')
            right_node_dis = abs(self.node_list[right].val - target) if right!=-1 else float('inf')
            if left_node_dis<right_node_dis:
                ans_list.append(self.node_list[left].val)
                left = left-1 if left>=1 else -1
            else:
                ans_list.append(self.node_list[right].val)
                right = right+1 if right<(n-1) else -1
            
            k -= 1
        return ans_list

    
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left) 
            res.append(root)
            res = res + self.inorderTraversal(root.right)
        return res
        