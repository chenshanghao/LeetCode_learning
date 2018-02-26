class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        self.dfs(nums, result)
        return result
        
    
    def dfs(self, nums, result):
        if nums not in result:
            result.append(nums)
        if len(nums) == 1:
            return
        for i in range(len(nums)):
            self.dfs(nums[0:i] + nums[i+1:len(nums)], result)
        
        