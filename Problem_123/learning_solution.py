# First assume that we have no money, so buy1 means that we have to borrow money from others, 
# we want to borrow less so that we have to make our balance as max as we can(because this is negative).

# sell1 means we decide to sell the stock, after selling it we have price[i] money and we have to give back the money we owed,
#  so we have price[i] - |buy1| = prices[i ] + buy1, we want to make this max.

# buy2 means we want to buy another stock, we already have sell1 money, 
# so after buying stock2 we have buy2 = sell1 - price[i] money left, we want more money left, so we make it max

# sell2 means we want to sell stock2, we can have price[i] money after selling it, 
# and we have buy2 money left before, so sell2 = buy2 + prices[i], we make this max.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell1, sell2 = 0, 0
        buy1, buy2 = float('-inf'), float('-inf')
        for i in range(len(prices)):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 =max(sell2, buy2 + prices[i])
        return sell2