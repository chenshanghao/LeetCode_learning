# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
    
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # write your code here
        if root is None:
            return []
        # 根据count来追踪层，偶数层则反转
        count = 1
        result = []
        
        q = Queue.Queue()
        q.put(root)
        
        while not q.empty():
            size = q.qsize()
            sub = []
            for i in range(size):
                node = q.get()
                sub.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            if count%2 == 0:
                sub = sub[::-1]
            count+=1
            result.append(sub)
            
        return result