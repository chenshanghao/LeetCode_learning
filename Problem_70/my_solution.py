class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        
        results = [1, 1, 2]
        
        for i in range(3, n):
            results.append(results[i - 1] + results[i - 2])
        return results[n - 1] + results[n - 2]
        
            
        