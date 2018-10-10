class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        a, b = [nums[0]], [0]
        for i in range(1,n):
            a.append(max(b[i-1] + nums[i], a[i-1]))
            b.append(a[i-1])
        return max([max(a), max(b)])
        