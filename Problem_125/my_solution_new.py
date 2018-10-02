class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str 
        :rtype: bool
        """
        # attention
        # 1.  alphanumeric -> 数字和字母 s[i].isalnum()
        #.2.  判断不能跳出边界  
        n = len(s)
        if n <= 1:
            return True
        i, j = 0, n-1
        while(i < j):
            while(i < j and s[i].isalnum() == False):
                i += 1
            while(i <j and s[j].isalnum() == False):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True