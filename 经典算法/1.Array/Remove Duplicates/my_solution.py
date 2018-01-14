class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return nums
        i= 0
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                pass
            else:
                i += 1
                nums[i] = nums[j]
        return nums[0:i+1]