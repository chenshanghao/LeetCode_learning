class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # quotient 商
        # denominator 余数
        # divmod return quotient, denominator
        sign = '-' if numerator * denominator < 0 else ''
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        result_list = [sign, str(quotient), '.']
        remainders = []
        while remainder not in remainders:
            remainders.append(remainder)
            quotient, remainder = divmod(remainder * 10, abs(denominator))
            result_list.append(str(quotient))

        idx = remainders.index(remainder)
        result_list.insert(idx + 3, '(')
        result_list.append(')')
        
        # Input 2  1  Output 2. shold use rstrip
        result = ''.join(result_list).replace('(0)', '').rstrip('.')
        return result