class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        min_sum, min_index, total = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if min_sum > total:
                min_sum, min_index = total, i + 1
        return min_index
        
        