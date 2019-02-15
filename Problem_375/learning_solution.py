
# 這題要求我們在猜測數字y未知的情況下（1~n任意一個數），要我們在最壞情況下我們支付最少的錢。也就是說要考慮所有y的情況。

# 我們假定選擇了一個錯誤的數x，（1<=x<=n && x!=y ）那麼就知道接下來應該從[1,x-1 ] 或者[x+1,n]中進行查找。
# 假如我們已經解決了[1,x-1] 和 [x+1,n]計算問題，我們將其表示爲solve(L,x-1)
# 和solve(x+1,n)，那麼我們應該選擇max(solve(L,x-1),solve(x+1,n))
# 這樣就是求最壞情況下的損失。總的損失就是 f(x) = x + max(solve(L,x-1),solve(x+1,n))


# 那麼將x從1~n進行遍歷，取使得 f(x) 達到最小，來確定最壞情況下最小的損失，也就是我們初始應該選擇哪個數。

# 上面的說法其實是一個自頂向下的過程（Top-down），可以用遞歸來解決。很容易得到如下的代碼（這裏用了記憶化搜索）：



class Solution:
    def getMoneyAmount(self, n: 'int') -> 'int':
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for l in range(n-1, 0, -1):
            for r in range(l+1, n + 1):
                for i in range(l, r):
                    if l>=r:
                        dp[l][r] = 0
                    else:
                        if dp[l][r] == 0:
                            dp[l][r] = i+max(dp[l][i-1], dp[i+1][r])
                        else:
                            dp[l][r] = min(i+max(dp[l][i-1], dp[i+1][r]), dp[l][r])
        return dp[1][n]
        

