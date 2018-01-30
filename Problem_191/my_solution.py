
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_value = bin(n)
        result = 0
        for i in range(2, len(bin_value)):
            if bin_value[i] == "1":
                result += 1
        return result