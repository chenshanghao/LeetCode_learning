class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0
        elif m < n:
            return -1
        for i in range(m -n + 1):
            if haystack[i] == needle[0]:
                j = 0
                while(j < n):
                    if haystack[i+j] != needle[j]:
                        break
                    else:
                        j += 1
                if j == n:
                    return i
        return -1
            
        