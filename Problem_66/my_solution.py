class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        digits[n - 1] += 1
        
        k = n -1
        while( digits[k] > 9 and k > 0):
            digits[k] = digits[k] % 10
            digits[k - 1] += 1
            k -= 1
        if k == 0 and digits[k] > 9:
            digits[0] = digits[0] % 10
            digits.insert(0, 1)
        return digits
        