class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits interger max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while(b != 0):
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative

        # >>  右移
        # <<  左移
        # |   位或 
        # &   位与
        # ^   位异或
        # ~   非

        return a if a <= MAX else ~(a ^ mask)