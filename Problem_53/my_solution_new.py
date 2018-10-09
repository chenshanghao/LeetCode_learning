class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        ans = [nums[0]]
        for i in range(1, n, 1):
            if ans[i-1]<= 0:
                ans.append(nums[i])
            else:
                ans.append(nums[i] + ans[i-1])
        return max(ans)