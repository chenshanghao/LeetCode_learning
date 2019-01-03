class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        n = len(s)
        if n == 0:
            return ans
        DP =[[0 for i in range(n)] for _ in range(n)]
        
        max_len = 1
        ans = s[0]
        for i in range(n):
            DP[i][i] = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                DP[i][i+1] = True
                max_len = 2
                ans = s[i:i+2]
        
        # 遍历设定DP[][] 数组
        for j in range(1,n):
            for i in range(0, j-1):
                if s[i] == s[j] and DP[i+1][j-1]:
                    DP[i][j] = True
                    if max_len < j - i + 1:
                        ans = s[i:j+1]
                        max_len = j - i + 1
        return ans
                        
        
        