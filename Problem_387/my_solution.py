class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_char_num = {}
        n = len(s)
        for i in range(n):
            if s[i] in dict_char_num:
                dict_char_num[s[i]] += 1
            else:
                dict_char_num[s[i]] = 1
        for i in range(n):
            if dict_char_num[s[i]] == 1:
                return i
        return -1