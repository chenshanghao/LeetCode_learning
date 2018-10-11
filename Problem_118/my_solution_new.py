class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            new_list = [ans[i-1][0]]
            for j in range(len(ans[i-1]) - 1):
                new_list.append(ans[i-1][j] + ans[i-1][j+1])
            new_list.append(ans[i-1][-1])
            ans.append(new_list)
        return ans
                
        