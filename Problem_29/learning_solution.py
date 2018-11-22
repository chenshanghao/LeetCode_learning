class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 1. +,-
        # 2. 越界
        # 3 = 0
        # 4. 正常
# 1.利用减法，将被除数减去除数，减去的次数累计即为最后结果

# 2.为了解决效率问题，可以减去除数的倍数，利用位运算，每次除数左移一位（2倍），次数相应加对应的倍数。

# 3.如果左移一位的除数过大，除数还原。

# 4.注意处理除法运算中正负号的问题。

        pos = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend - tmp >= 0:
                dividend -= tmp
                result += i
                i <<= 1
                tmp <<= 1
        if not pos:
            result = -result
        return min(2147483647, max(result, -2147483648))
         
        
        