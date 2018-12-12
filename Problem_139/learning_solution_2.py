class Solution:
    
    # recursion formula                True    if dp[0,i] == True and s[i,j] in worDict (0<=i<j)
    #                   dp[0,j] =      False
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False]*(n+1)
        wordDict=set(wordDict)
        dp[0] = True
        for i in range(n):
            for j in range(i,-1,-1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1] = True
                    break
        return dp[n]
        