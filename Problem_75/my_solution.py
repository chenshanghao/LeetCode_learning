class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_red, len_white, len_blue = 0, 0, 0
        for i in nums:
            if i == 0:
                len_red += 1
            elif i == 1:
                len_white += 1
            elif i == 2:
                len_blue += 1 
        for i in range(len(nums)):
            if i < len_red:
                nums[i] = 0
            elif i < (len_red + len_white):
                nums[i] = 1
            else:
                nums[i] = 2  