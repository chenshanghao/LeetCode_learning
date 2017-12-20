class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        if len_s == 0:
            return 0
        
        sub_max,word_index_dict = {}, {}
        sub_max[0] = s[0]
        word_index_dict[s[0]] = 0
        for i in range(1,len_s):
            if s[i] not in sub_max[i-1]:
                sub_max[i] = ''.join([sub_max[i-1],s[i]])
                word_index_dict[s[i]] = i
            else:
                sub_max[i] = s[word_index_dict[s[i]]+1 : i+1]
                word_index_dict[s[i]] = i
                        
                    
        longest_len,longest_index = 1, 0
        
        for key in sub_max.iterkeys():
            if len(sub_max[key]) > longest_len:
                longest_len = len(sub_max[key])
                longest_index = key
        
        return longest_len
        
        
                
            