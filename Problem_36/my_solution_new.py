class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # test row
        for i in range(len(board)):
            if self.isValidList(board[i]) == False:
                return False
        # test cow
        for i in range(len(board)):
            test_list = []
            for j in range(len(board)):
                test_list.append(board[j][i])
            if self.isValidList(test_list) == False:
                return False
        # test sub-box
        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                test_list = []
                test_list = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                if self.isValidList(test_list) == False:
                    return False
        return True
                
    
    def isValidList(self, input_list):
        dict_list = []
        for i in input_list:
            if i in dict_list:
                return False
            elif i != ".":
                dict_list.append(i)
        return True
        