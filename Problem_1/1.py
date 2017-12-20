class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
        	if target - nums[i] in nums:
        		for k in range(i+1, len(nums)):
        			if nums[k] == (target - nums[i]):
        				return [i, k]
        return False