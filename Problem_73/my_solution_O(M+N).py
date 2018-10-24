class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # o(m+n)
        if len(matrix) == 0:
            return
        row_len, col_len = len(matrix), len(matrix[0])   
        zero_row = [0] * col_len
        zero_row_index, zero_col_index = [1] * row_len, [1] * col_len
        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0:
                    zero_row_index[i] = 0
                    zero_col_index[j] = 0
        for i in range(row_len):
            if zero_row_index[i] == 0:
                matrix[i] = zero_row
        for j in range(col_len):
            if zero_col_index[j] == 0:
                for i in range(row_len):
                    matrix[i][j] = 0
            
        