class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        cur, profit = 0, 0
        for tail in range(1,len(prices)):   
            if prices[cur] >= prices[tail]:
                cur = tail
            else:
                if (tail < len(prices)-1 and prices[tail]>=prices[tail+1]) or (tail == len(prices) -1):
                    profit += prices[tail]-prices[cur]
                    cur=tail+1
        return profit

                


        