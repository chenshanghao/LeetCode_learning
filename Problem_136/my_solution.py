class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_num_val = {}
        for i in range(len(nums)):
            if nums[i] in dict_num_val:
                dict_num_val[nums[i]] += 1
            else:
                dict_num_val[nums[i]] = 1
        for key in dict_num_val:
            if dict_num_val[key] == 1:
                return key