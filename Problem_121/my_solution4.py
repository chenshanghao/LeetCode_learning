class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        n = len(prices)
        if n<=1:
            return 0
        
        profit = [0]* n
        min_value = prices[0]
        
        for i in range(1,n):
            if prices[i] - min_value > 0:
                profit[i] = prices[i] - min_value 
            
            if prices[i] < min_value:
                min_value = prices[i]
        
        return max(profit)