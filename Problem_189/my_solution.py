class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        nums = self.reverse(nums, 0, n-k-1)
        nums = self.reverse(nums, n-k, n-1)
        nums = self.reverse(nums, 0, n-1)

    
    def reverse(self, array, start, end):
        while(start < end):
            array[start] ^= array[end]
            array[end] ^= array[start]
            array[start] ^= array[end]
            start += 1
            end -= 1
        return array