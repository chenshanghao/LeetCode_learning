class Solution:
    def combinationSum3(self, k: 'int', n: 'int') -> 'List[List[int]]':
        result=[]
        candidates = [i for i in range(1,10)]
        self.helper(k, n, candidates, result, 0, [])
        return result
    
    def helper(self, k, n, candidates, result, start, tmp):
        if sum(tmp) == n and len(tmp) == k:
            result.append(tmp[:])
            return
        if sum(tmp) >= n or len(tmp) >= k:
            return
        
        for i in range(start, len(candidates)):
            tmp.append(candidates[i])
            self.helper(k, n, candidates, result, i+1, tmp)
            tmp.pop()