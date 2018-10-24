class Solution(object):
    def longestPalindrome(self, s):
        ans = ''
        max_len = 0
        n = len(s)
        # 设定动态规划数组
        DP = [[0] * n for _ in range(n)]

        # 设定所有 DP[i][i] = True
        for i in range(n):
            DP[i][i] = True
            max_len = 1
            ans = s[i]

        # 设定所有 DP[i][i+1]
        for i in range(n-1):
            if s[i] == s[i+1]:
                DP[i][i+1] = True
                ans = s[i:i+2]
                max_len = 2

        # 遍历设定DP[][] 数组
        for j in range(n):
            for i in range(0, j-1):
                if s[i] == s[j] and DP[i+1][j-1]:
                    DP[i][j] = True
                    if max_len < j - i + 1:
                        ans = s[i:j+1]
                        max_len = j - i + 1
        return ans