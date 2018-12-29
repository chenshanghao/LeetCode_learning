class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        point = '.'
        for i in range(9):
            row = []
            column = []
            square = []
            for j in range(9):
                row_element = board[i][j]
                if row_element != point:
                    if row_element in row:
                        return False
                    else:
                        row.append(row_element)
                col_element = board[j][i]
                if col_element != point:
                    if col_element in column:
                        return False
                    else:
                        column.append(col_element)
                    
                box_element = board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]
                if box_element != point:
                    if box_element in square:
                        return False
                    else:
                        square.append(box_element)
        return True
        