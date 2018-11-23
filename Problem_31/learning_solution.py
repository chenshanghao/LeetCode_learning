class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Example  6   9   7   4   3   2
        # Step 1   *6* 8   7   4   3   2
        # Step 2   6   8  *7*  4   3   2
        # Step 3   7  *8   6   4   3   2*
        # Step 4   7   2   3   4   6   8
        n=len(nums)
        if n <=1:
            return
        i = n-1
        while i-1 >= 0 and nums[i] <= nums[i-1]:
            i-=1
        if i>0:
            j = n-1
            while j>=i:
                if nums[j] > nums[i-1]:
                    nums[j], nums[i-1] = nums[i-1],nums[j]
                    break
                j-=1
            
        m = n-1
        while i<m:
            nums[i], nums[m] = nums[m], nums[i]
            i+=1
            m-=1
        