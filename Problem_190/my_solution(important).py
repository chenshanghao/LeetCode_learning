class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result = result + (1 & n)  # 括号至关重要
            n = n >> 1
            if i < 31:
                result = result << 1
        return result