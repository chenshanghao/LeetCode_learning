class Solution(object):
    def maxSubArray(self, nums):
        for i in xrange(1,len(nums)):
            nums[i]=max(nums[i], nums[i]+nums[i-1])
        return max(nums)