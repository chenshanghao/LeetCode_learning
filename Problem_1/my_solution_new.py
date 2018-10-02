class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Attention:
        # 1. you may not use the same element twice.
        dict_value_index = {}
        for i in range(len(nums)):
            if target - nums[i] in dict_value_index:
                return [dict_value_index[target - nums[i]], i]
            dict_value_index[nums[i]]=i
                
        