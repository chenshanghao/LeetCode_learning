class Solution:
    """
    @param s: a string
    @return: reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order
    """
    def reverseWords(self, s):
        # Write your code here
        s = s.split(" ")
        n = len(s)
        res = ''
        for i in range(n-1):
            res += s[i][::-1] + " "
        res += s[n-1][::-1]
        return res