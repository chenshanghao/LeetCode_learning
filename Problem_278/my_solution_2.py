class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1,1]
        for i in range(2,n+1):
            res.append(res[i-2] + res[i-1])
        return res[n]
        