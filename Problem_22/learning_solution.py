class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        if n==0:    return ans
        self.dfs('', 2*n, ans)
        return ans
    def dfs(self, string, length, ans):
        if len(string) == length:
            ans.append(string) 
            return
        if string.count('(') < length/2:
            self.dfs(string+'(',length,ans)
        if string.count('(') > string.count(')'):
            self.dfs(string+')',length,ans)
        
        
        
        