class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_nums = {}
        for index, num in enumerate(nums):
        	if target - nums[index] in dict_nums:
        		return [index, dict_nums[target - nums[index]]]
        	else:
        		dict_nums[num] = index