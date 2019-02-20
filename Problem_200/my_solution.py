class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        ans = 0
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans+=1
                    self.helper(i, j, m, n, grid)
        return ans
    
    def helper(self, i, j, m, n, grid):
        if i<0 or j<0 or i>=m or j>=n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.helper(i-1,j, m, n, grid)
        self.helper(i+1,j, m, n, grid)
        self.helper(i,j-1, m, n, grid)
        self.helper(i,j+1, m, n, grid)        