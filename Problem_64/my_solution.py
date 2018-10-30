class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        a = [[0 for i in range(n)] for j in range(m)]
        a[0][0] = grid[0][0]
        
        for i in range(1, m):
            a[i][0] = a[i-1][0] + grid[i][0]
        
        for j in range(1, n):
            a[0][j] = a[0][j-1] + grid[0][j]
            
        for i in range(1, m):
            for j in range(1, n):
                a[i][j] = min(a[i-1][j], a[i][j-1]) + grid[i][j]
        
        return a[m-1][n-1]
        