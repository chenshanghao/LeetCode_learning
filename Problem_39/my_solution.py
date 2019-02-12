class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        self.result = []
        self.helper(candidates, target, 0, [])
        return self.result
    
    def helper(self, candidates, target, start, temp):
        if sum(temp) == target:
            self.result.append(temp)
            return
        if sum(temp) > target:
            return
        
        for i in range(start, len(candidates)):
            temp.append(candidates[i])
            self.helper(candidates, target, i, temp[:])
            temp.pop()
            
        