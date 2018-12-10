class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        self.result = []
        self.helper('', s)
        return len(self.result)
    
    def helper(self, temp, s):
        if len(s) == 0:
            self.result.append(temp)
            return
        if s[0]=='0':
            return
        elif len(s) == 1:
            self.result.append(temp+s[0])
        else:
            if ((int(s[0]))*10+int(s[1])) <= 26:
                self.helper(temp+s[0],s[1:])
                self.helper(temp+s[0]+s[1], s[2:])
            else:
                self.helper(temp+s[0],s[1:])
                