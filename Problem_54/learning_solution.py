class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 控制好当前遍历的边界，不断的向内缩进。需要注意的是，缩到最里面的时候可能会出现以下几种情况：
        # 1.中心只剩下一个数值
        # example           last:
        #     1 2 3         
        #     4 5 6                5
        #     7 8 9        
        
        # 2.中心横向多个数值
        #   1  2  3  4  5  6            Last:
        #   7  8  9  10 11 12                   8 9 10 11
        #   13 14 15 16 17 18
        
        # 3.中心纵向多个数值
        #   1  2  3           Last:
        #   4  5  6                  5
        #   7  8  9                  8
        #  10  11 12
        
        ## 4. Not value
        # 1  2
        # 3  4
        
        result = []
        if not matrix:
            return result
        
        top, left = 0, 0
        right, bottom = len(matrix[0])-1, len(matrix) -1
        
        while left<right and top<bottom:
            for i in range(left, right):
                result.append(matrix[top][i])
            for i in range(top, bottom):
                result.append(matrix[i][right])
            for i in range(right,left,-1):
                result.append(matrix[bottom][i])
            for i in range(bottom,top,-1):
                result.append(matrix[i][left])
            left, top = left+1, top+1
            right, bottom = right-1, bottom-1
            
        # 1. only one value
        if left == right and top == bottom:
            result.append(matrix[top][left])
        # 2. left to right value
        elif left == right:
            for i in range(top, bottom+1):
                result.append(matrix[i][left])
        # 3. top to bottom value
        elif  top == bottom:
            for i in range(left,right+1):
                result.append(matrix[top][i])
        return result