class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.helper(nums, [], result)
        return result
    
    def helper(self, s, tmp,result):
        if len(tmp) == len(s):
            result.append(tmp[:])
        
        for i in s:
            if i in tmp:
                continue
            tmp.append(i)
            self.helper(s,tmp,result)
            tmp.pop()