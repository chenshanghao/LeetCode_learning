class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        small = big = float('-inf')
        for value in nums:
            if value < small:
                small = value
            elif value <= big:
                big = value
            else:
                return True
        return False
                