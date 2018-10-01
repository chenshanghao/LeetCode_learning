class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        k = k%len(nums)
        nums[:] = nums[-k:]+nums[0:len(nums)-k]
        
        
        #1.错误1
        # nums[:] = nums[n-k:] + nums[:n-k] 
        # nums = nums[n-k:] + nums[:n-k]
        # The previous one can truly change the value of old nums, 
        # but the following one just changes its reference to a new nums not the value of old nums.
        
        #2.错误2
        # nums[:] = nums[-k:]+nums[0:len(nums)-k]