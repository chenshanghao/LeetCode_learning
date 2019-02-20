class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        self.res = []
        if n == 0:
            return self.res
        self.helper(0, 0, n, '')
        return self.res
    
    def helper(self, left, right, n, temp):
        if left == right and left == n:
            self.res.append(temp[:])
            return
        
        if left < right:
            return
        
        if left < n:
            temp +='('
            self.helper(left+1, right, n, temp)
            temp = temp[:-1]
        
        if left>right:
            temp += ')'
            self.helper(left, right+1, n, temp)
            temp = temp[:-1]
        