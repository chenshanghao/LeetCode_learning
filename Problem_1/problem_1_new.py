class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_index_value = {}
        for i in range(len(nums)):
            if target - nums[i] in dict_index_value:
                return [i, dict_index_value[target - nums[i]]]
            # 为什么要先计算呢？ 考虑一下
            dict_index_value[nums[i]] = i
            
            # Wrong experience
            # Input [3, 2, 4], 6
            # Output [0, 0]
                
        