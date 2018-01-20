class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low, result = 0, 0
        for i in range(len(prices)):
            if prices[i] < prices[low]:
                low = i
            elif prices[i] - prices[low] > result:
                result = prices[i] - prices[low]
        
        return result