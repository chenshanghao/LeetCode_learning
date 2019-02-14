class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        result = []
        self.helper(result, sorted(candidates), target, [], 0)
        return result
    
    def helper(self, result, candidates, target, tmp, start):
        if sum(tmp) == target:
            result.append(tmp[:])
            return
        if sum(tmp) > target:
            return
        
        for i in range(start, len(candidates)):
            tmp.append(candidates[i])
            self.helper(result, candidates, target, tmp, i)
            tmp.pop()