class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        max_list = [nums[0]]
        for i in range(1, n):
            max_list.append(max(max_list[i-1] + nums[i], nums[i]))
        return max(max_list)
        