class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n == 0:
            return ''
        common_prefix = strs[0]
        for i in range(1, n):
            for j in range(len(common_prefix)):
                if j < len(strs[i]) and common_prefix[j] == strs[i][j]:
                    continue
                else:
                    common_prefix = common_prefix[:j]
                    break
                if len(common_prefix) == 0:
                    return common_prefix
        return common_prefix
        
        