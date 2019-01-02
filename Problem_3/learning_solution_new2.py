class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = len_max = 0
        char_dict = {}
        for i in range(len(s)):
            if s[i] in char_dict and start <= char_dict[s[i]]:
                start = char_dict[s[i]] + 1
            else:
                len_max = max(len_max, i - start + 1)
            char_dict[s[i]] = i
        return len_max
                
                
            
        