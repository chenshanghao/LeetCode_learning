class Solution:
    def minimumTotal(self, triangle: 'List[List[int]]') -> 'int':
        n = len(triangle)
        dp = triangle[n-1]
        
        for row in range(n-2, -1, -1):
            for i in range(row+1):
                dp[i] = min(dp[i], dp[i+1]) + triangle[row][i]
        return dp[0]