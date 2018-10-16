class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        m = sum(nums)
        if n > 0:
            return (n+1)*n/2 - m
        else:
            return 0