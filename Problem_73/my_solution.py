class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        row_len, col_len = len(matrix[0]), len(matrix)
        row_zero, col_zero = [], []
        for row_index, row in enumerate(matrix):
            for col_index, value in enumerate(row):
                if value == 0:
                    if col_index not in col_zero:
                        col_zero.append(col_index)
                    if row_index not in row_zero:
                        row_zero.append(row_index)
        
        for i in row_zero:
            matrix[i] = [0] * row_len

        for j in col_zero:
            for i in range(col_len):
                matrix[i][j] = 0
            
        