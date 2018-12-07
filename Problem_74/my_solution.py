class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row_len = len(matrix)
        col_len = len(matrix[0])
        if (not row_len) or (not col_len):
            return False
        
        row_target = 0
        for i in range(row_len-1):
            if target>= matrix[i][0] and target< matrix[i+1][0]:
                row_target = i
                break
                       
        if row_target == 0 and target <= matrix[0][col_len-1]:
            row_target = 0
        elif row_target == 0 and target <= matrix[row_len-1][col_len-1]:
            row_target = row_len-1
        
        for i in range(col_len):
            if matrix[row_target][i] == target:
                return True
            if matrix[row_target][i] > target:
                return False
        return False