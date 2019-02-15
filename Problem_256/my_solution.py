class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        n = len(costs)
        if n == 0:
            return 0
        dp = [costs[0][0], costs[0][1], costs[0][2]]
        
        for i in range(1,n):
            temp_dp = [0,0,0]
            temp_dp[0] = min(dp[1], dp[2]) + costs[i][0]
            temp_dp[1] = min(dp[0], dp[2]) + costs[i][1]
            temp_dp[2] = min(dp[0], dp[1]) + costs[i][2]
            dp = temp_dp
        return min(dp)
            
