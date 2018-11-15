class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        if len(candidates) == 0:
            return self.result
        self.backtrack(0, sorted(candidates), [], target)
        return self.result
        
    def backtrack(self, start, S, temp, target):
        sum_value = sum(temp)
        if sum_value == target:
            self.result.append(temp[:])
        if sum_value >= target:
            return
        
        for i in range(start, len(S)):
            temp.append(S[i])
            self.backtrack(i, S, temp, target)
            temp.pop()