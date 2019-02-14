import math

class Solution:
    """
    @param n: a integer
    @return: return a 2D array
    """
    def getFactors(self, n):
        # write your code here
        result = []
        if n<=1:
            return result
        factor_list = self.findfactor(n)
        self.helper(n, [], 0, result, factor_list)
        return result
    
    def helper(self, n, tmp, start, result, factor_list):
        if n == 1 and len(tmp)>1:
            result.append(tmp[:])
            return
        for i in range(start, len(factor_list)):
            if n % factor_list[i] == 0:
                tmp.append(factor_list[i])
                self.helper(int(n/factor_list[i]), tmp, i, result, factor_list)
                tmp.pop()
    
    def findfactor(self, n):
        factor_list = []
        for i in range(2, int(n/2)+1):
            if n%i == 0:
                factor_list.append(i)
        return factor_list
            
            
        
        