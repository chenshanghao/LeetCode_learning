class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # For n=1:    0        1
        # For n=2:    00   01   10    11  (first two insert 0, last two insert 1)
        # For n=3:    000  001  010  011  100  101  110 111(first four insert 0, last four insert 1)
        
        if n<=0:
            return [0]
        res = [0, 1]
        
        for i in range(2, n+1):
            for j in range(len(res)-1, -1, -1):
                res.append(res[j] | 1<<i-1)
        return res
        