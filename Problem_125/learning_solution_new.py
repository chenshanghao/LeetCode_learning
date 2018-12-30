class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphanumerics = [c.lower() for c in s if c.isalnum()]
        return alphanumerics[::-1] == alphanumerics