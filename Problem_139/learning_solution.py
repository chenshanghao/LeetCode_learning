class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.m ={}
        return self.canBreak(s, self.m, set(wordDict))   
    def canBreak(self,s, m, wordDict):
        if s in m:
            return m[s]
        if s in wordDict:
            m[s] = True
            return True
        for i in range(1, len(s)):
            if (s[0:i] in wordDict) and (self.canBreak(s[i:], self.m, wordDict)):
                m[s] = True
                return True
        m[s] = False
        return False