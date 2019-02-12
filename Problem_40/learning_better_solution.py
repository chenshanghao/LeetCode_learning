class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        if len(candidates) == 0:
            return self.result
        self.backtrack(sorted(candidates), target, [], 0)
        return self.result
    
    def backtrack(self, candidates, target, temp, start):
        if sum(temp) > target:
            return
        if sum(temp) == target:
            self.result.append(temp[:])
            return
        for i in range(start, len(candidates)):
            if i>start and candidates[i] == candidates[i-1]:
                continue
            temp.append(candidates[i])
            self.backtrack(candidates, target, temp, i+1)
            temp.pop()
            
    