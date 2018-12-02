class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 1.奇数, 需要填充中心店
        # 2.偶数
        
        result = [[0 for i in range(n)] for j in range(n)]
        left, top = 0, 0
        right, bottom = n-1, n-1
        value = 1
        
        while(left<right and top<bottom):
            for i in range(left, right):
                result[top][i]=value
                value += 1
            
            for i in range(top, bottom):
                result[i][right]=value
                value+=1
            
            for i in range(right, left, -1):
                result[bottom][i]=value
                value+=1
            
            for i in range(bottom,top,-1):
                result[i][left]=value
                value+=1
                
            left,top = left+1, top+1
            right,bottom = right-1, bottom-1
            
        if n%2 == 1:
            result[top][left] = value
        return result
        
        