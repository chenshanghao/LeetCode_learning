class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        c, d, e = [], [], []
        for i in range(9):
            
            #横
            if self.isValidList(board[i]) == False:
                return False
            
            #竖
            a = []
            for j in range(9):
                a.append(board[j][i])
            if self.isValidList(a) == False:
                return False
        
            c.append(board[i][0])
            c.append( board[i][1])
            c.append(board[i][2])
            
            d.append(board[i][3])
            d.append(board[i][4])
            d.append(board[i][5])
          
            e.append(board[i][6])
            e.append(board[i][7])
            e.append(board[i][8])
            # print(c)
            # print(d)
            # print(e)
            
            if(i + 1) % 3 == 0:
                if self.isValidList(c) == False or self.isValidList(d) == False or self.isValidList(e) == False:
                    return False
                else:
                    c, d, e = [], [], []
            
                
            
            
        return True
        
    def isValidList(self, nums):
        nums2 = []
        for i in nums:
            if i != u".":
                if i in nums2:
                    # print(nums)
                    return False
                else:
                    nums2.append(i)
        return True
        