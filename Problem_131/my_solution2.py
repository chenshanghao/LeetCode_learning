class Solution:
    def partition(self, s: 'str') -> 'List[List[str]]':
        result = []
        self.helper(s,0,[],result)
        return result
    
    def helper(self, s, start, tmp,result):
        if start == len(s):
            result.append(tmp[:])
        for i in range(start, len(s)):
            if self.isPalindrome(s[start:i+1]):
                tmp.append(s[start:i+1])
                self.helper(s,i+1,tmp,result)
                tmp.pop()
    
    def isPalindrome(self, s):
        if len(s) <=1:
            return True
        l,r = 0,len(s)-1
        while(l<r):
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
            
        