class Solution:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        if amount == 0:
            return 0
        coins = sorted(coins)
        dp = [float('inf')]*(amount+1)
        for i in coins:
            if i > amount:
                break
            dp[i] = 1
        
        for i in range(coins[0], amount+1):
            if dp[i] == 1:
                    continue
            for j in coins:
                if i-j<1:
                    break
                if dp[i-j]!=float('inf') :
                    dp[i] = min(dp[i], 1+ dp[i-j])
        
        return dp[amount] if dp[amount]!=float('inf') else -1
                
                