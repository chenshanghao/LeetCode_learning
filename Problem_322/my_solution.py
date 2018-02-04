import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount <= 0:
            return 0
        change_value = [0] * (amount + 1)
        for i in range(len(coins)):
            if coins[i] <= amount:
                change_value[coins[i]] = 1
        for i in range(1, amount+1):
            if change_value[i] != 1:
                change_value[i] = sys.maxint
            for j in coins:
                if (i - j >= 0) and change_value[i - j] != -1:
                    change_value[i] = min(change_value[i - j] + 1, change_value[i])
            if change_value[i] == sys.maxint:
                change_value[i] = -1
        return change_value[amount]
            
            

            
        