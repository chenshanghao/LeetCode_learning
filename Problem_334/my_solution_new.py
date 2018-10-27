class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        small_index, large_index = 0, 0
        for index, value in enumerate(nums):
            if value < nums[small_index]:
                small_index = index
            elif value > nums[small_index] and (value < nums[large_index] or large_index == 0):
                large_index = index
            else:
                if value > nums[large_index] and large_index != 0:
                    return True
        return False