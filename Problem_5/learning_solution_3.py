class Solution(object):

    def __init__(self):
        self.logestSize = 0
        self.longestSrart= 0

    def longestPalindrome(self, s):
        for index, value in enumerate(s):
            self.checkEvenPalindrome(s, index)
            self.checkOddPalindrome(s, index)
        return s[self.longestSrart: self.longestSrart + self.logestSize+1]

    def checkOddPalindrome(self, s, index):
        start = index
        end = index

        #注意边界条件
        while start >=1 and end < len(s) - 1 and s[start -1] == s[end + 1]:
            start -= 1
            end += 1

        if end - start > self.logestSize:
            self.logestSize = end - start
            self.longestSrart = start


    def checkEvenPalindrome(self, s, index):
        start = index
        end = min(index+1, len(s) -1)
        while start >= 1 and end <= len(s)-1 and s[start-1]== s[end+1] and s[start]==s[end]:
            start -= 1
            end +=1

        if end -start > self.logestSize and s[start] == s[end]:
            self.logestSize = end - start
            self.longestSrart = start            
