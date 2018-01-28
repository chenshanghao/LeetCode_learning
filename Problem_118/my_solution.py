class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result =[[1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return result
        n = 1
        while(n < numRows):
            lastRow = result[n - 1]
            nextRow = [lastRow[0]]
            len_lastRow = len(result[n - 1])
            for i in range(1, len_lastRow):
                nextRow.append(lastRow[i] + lastRow[i-1])
            nextRow.append(lastRow[len_lastRow-1])
            result.append(nextRow)
            n += 1
        return result
        
        