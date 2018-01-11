class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a, len_b = len(a), len(b)
        len_max = max(len_a, len_b)
        
        result = ""
        carry = 0
        for i in range(len_max):
            x = int(a[len_a - i - 1]) if i < len_a else 0
            y = int(b[len_b - i - 1]) if i < len_b else 0
            
            sum_i = (x + y + carry) % 2
            carry = (x + y + carry) / 2
            result = str(sum_i) + result
            
        if carry == 1:
            return '1' + result
        else:
            return result