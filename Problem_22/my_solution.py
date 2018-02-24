class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n < 1:
            return result
        self.dfs('', n*2, result)
        return result
        
    def dfs(self, string, lenth, result):
        if len(string) == lenth:
            result.append(string)
            return
        if string.count('(') < lenth/2:
            self.dfs(string+'(', lenth, result)
        if string.count(')') < string.count('('):
            self.dfs(string+')',lenth, result)
        