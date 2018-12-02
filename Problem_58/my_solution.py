class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)-1
        if n < 0:
            return 0
        count = 0
        while(n>=0 and(not((s[n]>='a' and s[n]<='z') or (s[n]>='A' and s[n]<='Z')))):
            n-=1
        while(n>=0):
            if s[n] == ' ':
                break
            else:
                count += 1
            n -=1
        return count
        
        