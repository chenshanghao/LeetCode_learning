class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        n = len(strs)
        
        if n <= 0:
            return result
        
        min_len = len(strs[0])

        #find the minium len str in strs
        for i in range(n):
            min_len = min(len(strs[i]), min_len)
        
        out_flag = False
        for j in range(min_len):
            value = strs[0][j]
            for i in range(1, n):
                if strs[i][j] != value:
                    out_flag = True
                    break
            if out_flag == True:
                break
            else:
                result += value
        
        return result
            
                
        
        