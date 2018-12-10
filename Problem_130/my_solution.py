class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
# 直接去找被X包围的O比较麻烦，不如转换一下思路，找出哪些O是没有被X包围的。
# 首先在面板四周的O肯定是没有被X包围的，与它们相连的O也是没有被包围的，其它的O都是被X包围的。
# 问题简化为将与四周的O相连的O都找出来，这些点不用变，其它点都变为X。
# 首先将四周的O压入栈内，依次访问栈内元素，并将它们标记，
# 接着去判断它们四周的元素是否也是O，如果是且没有被标记过，则将其压入栈中。
# 当遍历完栈中的元素后，将有标记的元素变为O，其余都是X。
        if not board or not board[0]:
            return
        n = len(board)
        m = len(board[0])
        queue = []
        
        # Get all '0' on edge
        for i in range(n):
            for j in range(m):
                if ((i in (0, n-1)) or (j in (0, m-1))) and board[i][j] == 'O':
                    queue.append((i, j))
        
        # Mark all '0' which can connect to '0' on edge
        while(queue):
            r, c = queue.pop(0)
            if 0<=r<n and 0<= c< m and board[r][c] =='O':
                board[r][c] = 'M'
                if r-1>=0 and board[r-1][c] == 'O':
                    queue.append((r-1, c))
                if r+1 < n and board[r+1][c] == 'O':
                    queue.append((r+1, c))
                if c-1>=0 and board[r][c-1] == 'O':
                    queue.append((r, c-1))
                if c+1<m and board[r][c+1] =='O':
                    queue.append((r,c+1))
        
        # Update characters
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        