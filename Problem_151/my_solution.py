class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split()
        ret = ''
        if len(a) == 0:
            return ret
        
        for i in range(len(a)-1,0,-1):
            ret += (a[i] + ' ')
        ret += a[0]
        return ret