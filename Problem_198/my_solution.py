class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        results = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            results.append(max(nums[i] + results[i - 2], results[i - 1]))
        return max(results)