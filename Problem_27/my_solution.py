class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = len(nums)-1
        for index in range(len(nums), 0, -1):
            if nums[j] != val:
                break
            else:
                j = j-1
                
        for index, value in enumerate(nums):
            if index > j:
                break
            if value == val:
                nums[index], nums[j] = nums[j],nums[index]
                while(True):
                    j -=1
                    if nums[j] != val:
                        break
        return j+1