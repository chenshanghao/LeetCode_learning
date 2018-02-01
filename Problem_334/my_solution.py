class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        i, j, new_i = 0, 0, 0
        for index, value in enumerate(nums):
            if i == j and value <= nums[i]:
                i, j = index, index
            elif i == j and value > nums[i]:
                j = index
            
            if i < j and value > nums[j]:
                return True
            
            if i < j and value < nums[j] and value > nums[i]:
                j = index
            
            if i < j and value < nums[i] and value < nums[new_i]:
                new_i = index
                
            if i < j and nums[new_i] < value and value < nums[j]:
                i = new_i
                j = index
        return False
