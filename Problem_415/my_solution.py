class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len_num1, len_num2 = len(num1), len(num2)
        len_max = max(len_num1, len_num2)
        results = ''
        i, carry = 0, 0
        while(i < len_max):
            a = int(num1[len_num1 - i - 1]) if i < len_num1 else 0
            b = int(num2[len_num2 - i - 1]) if i < len_num2 else 0
            sum_num1_num2 = (a + b + carry) % 10
            carry = (a + b + carry) / 10
            results = str(sum_num1_num2) + results
            i += 1
            
        if carry == 1:
            return '1' + results
        else:
            return results