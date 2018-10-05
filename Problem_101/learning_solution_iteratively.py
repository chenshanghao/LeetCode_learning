# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution:
    # @param root, a tree node
    # @return a boolean
    def sym(self,left,right):
        if left==None and right==None:
            return True
        if left and right and left.val==right.val:
            return self.sym(left.left,right.right) and self.sym(left.right,right.left)
        else:
            return False
         
    #   如果是iterative的解法需要用两个stack去存node
    #   1.先将left 和right 依次存入stack1 stack2
    #   2.当stack非空的时候将node pop出来 依次往下取left 和right 


    def isSymmetric(self, root):
        if root==None:
            return True
        if root.left==None and root.right==None:
            return True
        if root.left==None or root.right==None:
            return False
        stack1=[]
        stack2=[]
        stack1.append(root.left)
        stack2.append(root.right)
        while len(stack1)!=0 and len(stack2)!=0:
            n1=stack1.pop()
            n2=stack2.pop()
            if n1.val!=n2.val:
                return False
            #if n1.left==None or n2.right==None:
             #   return False
            #if n1.right==None or n2.left==None:
             #   return False
            if n1.left==None and n2.right!=None or n1.left!=None and n2.right==None:
                return False
            if n1.right==None and n2.left!=None or n1.right!=None and n2.left==None:
                return False
            if n1.left and n2.right:
                stack1.append(n1.left)
                stack2.append(n2.right)
            if n1.right and n2.left:
                stack1.append(n1.right)
                stack2.append(n2.left)
        return True
