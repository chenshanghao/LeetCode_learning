class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        res = 0
        if n <= 1:
            return res
        i = 0
        for j in range(1, n):
            if prices[j] - prices[i] > 0:
                res = max(prices[j] - prices[i], res)
            else:
                i = j
        return res
        
        