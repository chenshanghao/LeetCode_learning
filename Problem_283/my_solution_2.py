class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        slow = fast = 0
        while fast<n:
            if slow != fast and nums[fast] != 0:
                nums[slow] = nums[fast]
                slow+=1
                fast+=1
            elif slow !=fast and nums[fast] ==0:
                fast += 1
            elif slow == fast and nums[slow] == 0:
                fast += 1
            else:
                fast +=1
                slow +=1
        while slow<n:
            nums[slow] = 0
            slow += 1
            
        