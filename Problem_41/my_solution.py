class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 1
        positive_dict = {}
        for i in nums:
            if i > 0:
                positive_dict[i] = True
        
        for i in range(1, n+1):
            if i not in positive_dict:
                return i
        return n+1
        
        
        