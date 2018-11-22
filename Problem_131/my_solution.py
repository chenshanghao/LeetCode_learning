class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.result = []
        if len(s) == 0: return self.result
        self.backtrack([],0,s)
        return self.result
        
    def IsPalindrome(self, string):
        i, j = 0, len(string)-1
        while(i<=j):
            if string[i]!= string[j]:
                return False
            i+=1
            j-=1
        return True
    
    def backtrack(self, temp, start, s):
        if start >= len(s):
            self.result.append(temp[:])
        for i in range(start,len(s)):
            if self.IsPalindrome(s[start:i+1]):
                temp.append(s[start:i+1])
                self.backtrack(temp, i+1, s)
                temp.pop()