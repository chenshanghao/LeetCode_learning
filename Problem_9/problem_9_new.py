class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x ==0:
            return True
        original_x = x
        reverse_x = 0
        while(x != 0):
            tail = x % 10
            reverse_x =  reverse_x*10 + tail
            x = x / 10
        if original_x == reverse_x:
            return True
        else:
            return False
        
        