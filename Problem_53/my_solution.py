class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        result = [nums[0]]
        
        for i in range(1, len(nums)):
            if result[i - 1] <= 0:
                result.append(nums[i])
            else:
                result.append(nums[i] + result[i - 1])
        return max(result)