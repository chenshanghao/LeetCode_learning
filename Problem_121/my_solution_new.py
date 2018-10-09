class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # initialize the n and ans
        n = len(prices)
        ans = 0
        # check the exception when the number of element is equal or smaller than 1
        if n <= 1:
            return ans
        i = 0
        
        # loop to update ans
        for j in range(1, n, 1):
            if prices[j] - prices[i] >= 0:
                ans = max(ans, (prices[j] - prices[i]))
            else:
                i = j
        return ans
         