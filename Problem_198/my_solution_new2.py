class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        if n<=2:
            return max(nums)
        ans = [nums[0], nums[1]]
        for i in range(2, n):
            ans.append(max(ans[i-2] + nums[i], ans[i-1]))
            ans[i-1] = max(ans[i-2], ans[i-1])
        return max(ans)

        