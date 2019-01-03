class Solution:
    """
    @param s: the given string
    @return: if the starting player can guarantee a win
    """
    def canWin(self, s):
        # write your code here
        # Solution 1:
        # Recursion
        # T(N) = (N - 1) * T(N - 2) = (N - 1) * (N - 3) * T(N - 4) = (N - 1)!!
        # canWin("++++++") = !canWin("--++++") || !canWin("+--+++") || !canWin("++--++") + || !canWin("+++--+") || !canWin("++++--")
        # canWin("--++++") = !canWin("----++") || !canWin("--+--+") || !canWin("--++--")
        # canWin("++++--") = !canWin("--++--") || !canWin("+--+--") || !canWin("++----")
        for i in range(1,len(s)):
            if s[i - 1] == "+" and s[i] == "+" and not self.canWin(s[:i-1] + "--" + s[i+1:]):
                return True 
        return False
        
        
        # Solution 2:
        memo = {}
        def canWin(self, s):
            # write your code here
            if s in self.memo:
                return self.memo[s]
            for i in range(len(s)-1):
                if s[i:i+2] == '++':
                    tmp = s[:i]+'--'+s[i+2:]
                    flag = self.canWin(tmp)
                    self.memo[tmp] = flag
                    if not flag:
                        return True
            return False