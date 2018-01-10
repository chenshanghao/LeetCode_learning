class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len_num1, len_num2 = len(num1), len(num2)
        results = 0
        for i in range(len_num1):
            for j in range(len_num2):
                results += int(num1[len_num1 - i - 1]) * int(num2[len_num2 - j - 1]) * (10**(i+j))
        
        return str(results)