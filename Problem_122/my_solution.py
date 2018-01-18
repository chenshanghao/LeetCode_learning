class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        low_flag = True
        buy_value, buy_index = prices[0], 0
        sell_value, sell_index = 0, 0
        results = 0

        for i in range(1,len(prices)):
            if low_flag == True:
                if prices[i] <= prices[i-1]:
                    buy_value = prices[i]
                    buy_index = i;
                else:
                    sell_value = prices[i]
                    sell_index = i
                    low_flag = False
            else:
                if prices[i] >= prices[i-1]:
                    sell_value = prices[i]
                    sell_index = i
                else:
                    results += (sell_value - buy_value)
                    buy_value = prices[i]
                    buy_index = i
                    low_flag = True
        if low_flag == False and (sell_index > buy_index):
            results += (sell_value - buy_value)
        return results
                    
                    
                