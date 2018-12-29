# Dynamic Programming Solution

# 1. 定义状态
# hold[i]: 第i天hold股票的最大profit
# unhold[i]: 第i天不hold股票的最大profit

# 2.Target
# unhold[n-1]

# 3. Base Case
# hold[0] = -prices[0]
# hold[1] = max(-prices[1], - prices[0])
# unhold[0] = 0

# 4. transfer equation
# hold[i] 取下列最大值
# 1. 第i天买入      unhold[i-2] - prices[i]
# 2. 第i天没有买入   hold[i-1]

# unhold[i] 取以下情况最大值
# 1. 第i天有卖出 hold[i-1] + prices[i]
# 2. 第i天没有卖出 unhold[i-1]


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        hold = [-prices[0]]
        unhold = [0]
        
        for i in range(1,n):
            if n==1:
                hold.append(max(hold[i-1], - prices[1]))
            else:
                hold.append(max(hold[i-1], unhold[i-2]-prices[i]))
            
            unhold.append(max(unhold[i-1],hold[i-1]+prices[i]))
        
        return unhold[n-1]
            