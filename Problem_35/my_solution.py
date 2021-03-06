class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        for index, value in enumerate(nums):
            if value >= target:
                return index
        return len(nums)
            
        