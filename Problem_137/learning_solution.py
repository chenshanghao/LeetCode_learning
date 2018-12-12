class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://leetcode.com/problems/single-number-ii/discuss/43360/The-simplest-solution-ever-with-clear-explanation
        b1, b0 = 0, 0
        for num in nums:
            b0 = (b0 ^ num) & (~b1)
            b1 = (b1 ^ num) & (~b0)
        return b0
        