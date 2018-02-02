class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_jump = 0
        len_nums = len(nums)
        for i in range(len(nums)):
            if i <= max_jump:
                max_jump = max(max_jump, i + nums[i])
            else:
                break
        return (max_jump >= len(nums) - 1)
                
            
            
        