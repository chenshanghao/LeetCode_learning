class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_array = len(nums)
        if len_array <= 1:
            return len_array
        cur_val = nums[0]
        poniter = 1
        num = 1
        for i in range(1, len_array):
            if nums[i] == cur_val:
                if num == 1:
                    num+=1
                    nums[poniter] = cur_val
                    poniter += 1
                elif num > 2:
                    num+=1
            else:
                nums[poniter] = nums[i]
                cur_val = nums[i]
                num = 1
                poniter += 1
        nums = nums[0: poniter]
        return poniter
                    
                
        