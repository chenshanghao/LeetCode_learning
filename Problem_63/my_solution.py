class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # if m > 0:
        #     n = len(obstacleGrid[0])
        #     if n == 0:
        #         return 0
        # else:
        #     return 0
        
        a = [[0 for t in range(n)]for i in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        # print(a)
        
        obstacle_flag = False
        for i in range(m):
            if obstacle_flag == False and obstacleGrid[i][0]==0:
                a[i][0] = 1
            else:
                a[i][0] = 0
                obstacle_flag = True
        # print(a)
        # print("******************")
             
        obstacle_flag = False
        for j in range(n):
            if obstacle_flag == False and obstacleGrid[0][j]==0:
                a[0][j] = 1
                print(a)
            else:
                a[0][j] = 0
                obstacle_flag = True
            
        # print("******************")
        # print(a)
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    a[i][j] = 0
                else:
                    a[i][j] = a[i-1][j] + a[i][j-1]
        # print(a)
        return a[m-1][n-1] 
                
            
                
            
        
        