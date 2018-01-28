class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_n = bin(n)[2:]
        len_n = len(bin_n)
        bin_n = (32 - len_n) * "0" + bin_n
        #reverse string
        bin_n = bin_n[::-1]
        return int(bin_n, 2)
        