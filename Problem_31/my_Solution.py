class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        #           *
        # step1   1 2 6 4 2 (from right to left)  
        # step2   1 2 2 4 6 (sorted left)
                    *   *
        # step3   1 2 2 4 6 (find the num)
        # step 4  1 4 2 2 6 (exchange the value )
        n = len(nums)
        if n<=1:
            return
        
        i = n-1
        while(i>0):
            if nums[i]> nums[i-1]:
                break
            i -= 1
            
        if i == 0:
            nums.sort()
            return
        
        i = i-1
        nums[i+1:] = sorted(nums[i+1:])
        
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i],nums[j]
                break
        