class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #attention
        #1. O(1) extra memory
        
        # current_position
        cur=0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[cur]<nums[i]:
                cur+=1
                nums[cur] = nums[i]
        return cur+1