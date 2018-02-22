#float('inf')   max_integer
#float('-inf')  -max_integer

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums == 0:
            return
        elif len_nums == 1:
            return 0
        nums.append(float('-inf'))
        nums.insert(0, float('-inf'))
        i = 1
        while(i <= len_nums):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i - 1
            i += 1
        return
            
        