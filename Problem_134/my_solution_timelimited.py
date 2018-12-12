class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        cost_remain = []
        for i in range(len(gas)):
            cost_remain.append(gas[i] - cost[i])
        cost_remain = cost_remain + cost_remain[:-1:]

        for i in range(len(gas)):
            for j in range(i+1,len(gas)+i+1):
                if sum(cost_remain[i:j]) < 0:
                    break
                if (j-i) == len(gas):
                    return i
        return -1
        
        