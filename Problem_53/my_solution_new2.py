class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        sum_list = [nums[0]]
        for i in range(1, n):
            if sum_list[i-1] + nums[i] > nums[i]:
                sum_list.append(sum_list[i-1] + nums[i])
            else:
                sum_list.append(nums[i])
        return max(sum_list)
            