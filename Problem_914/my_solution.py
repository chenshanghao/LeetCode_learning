class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        n = len(s)
        res = []
        for i in range(n-1):
            if s[i] == '+' and s[i+1] == s[i]:
                if i < (n-1):
                    res.append(s[0:i] + '--' + s[i+2:])
                else:
                    res.append(s[0:i] + '--')
        return res