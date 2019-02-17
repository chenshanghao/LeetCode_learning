class Solution:
    def maximalSquare(self, matrix: 'List[List[str]]') -> 'int':
        m = len(matrix)
        if not m:   return 0
        
        n = len(matrix[0])
        if not n:   return 0
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = matrix[0][0]
        max_value = 0
        
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0]>0:
                max_value = 1
        
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            if dp[0][j]>0:
                max_value = 1
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1
                    max_value = dp[i][j] if dp[i][j]>max_value else max_value
        return max_value*max_value