class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        elif n < m:
            return -1
        
        test_pos = 0
        while(test_pos < (n - m + 1)):
            if haystack[test_pos] == needle[0]:
                i, j = 0, test_pos
                while(j < (test_pos + m )):
                    if haystack[j] != needle[i]:
                        break
                    j += 1
                    i += 1
                if j == (test_pos + m ):
                    return test_pos
            test_pos += 1
        return -1
                        
            
                    
        