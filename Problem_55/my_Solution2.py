class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        max_step = []
        if nums[0] >= n-1:
            return True
        else:
            max_step.append(nums[0])
        maximum = nums[0]
        for i in range(1,n):
            if i <= maximum:
                maximum = max(i+nums[i], maximum)
                if maximum >= (n-1):
                    return True
            else:
                return False
        return False
            