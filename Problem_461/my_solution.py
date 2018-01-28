class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x, bin_y = bin(x)[2:], bin(y)[2:]
        i, j = len(bin_x) - 1, len(bin_y) - 1
        result = 0

        while(i >= 0 and j >= 0):
            if bin_x[i] != bin_y[j]:
                result += 1
            i -= 1
            j -= 1

        if i >= 0:
            result += bin_x[0:i + 1].count('1')
        elif j >= 0:
            result += bin_y[0:j + 1].count('1')
        return result
            
            
        
        
        