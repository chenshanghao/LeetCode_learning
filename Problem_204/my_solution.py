class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        result = [0] * (n)
        for i in range(2, n):
            if result[i] == 1:
                continue
            else:
                j = i
                while( j + i < n):
                    j = j + i
                    result[j] = 1
        result_num = 0 
        #print(result)
        for i in range(2, n):
            if result[i] == 0:
                result_num += 1
        return result_num
            
            
        
        