class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        len_x = len(x)
        if len_x == 0 or len_x ==1:
            return True
        j = len_x - 1
        is_palindrome = True
        for i in range(len_x/2):
            if x[i] == x[j]:
                i+=1;j-=1
            else:
                is_palindrome = False
                break
        return is_palindrome
        
        