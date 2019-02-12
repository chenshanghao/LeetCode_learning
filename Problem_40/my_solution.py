class Solution:
    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        self.result = []
        self.visited = [False] * len(candidates)
        self.helper(sorted(candidates), target, 0, [])
        return self.result
    
    def helper(self, candidates, target, start, temp):
        if sum(temp) == target:
            self.result.append(temp)
            return
        elif sum(temp) > target:
            return
        
        for i in range(start, len(candidates)):
            if self.visited[i]:
                continue
            if i>0 and candidates[i] == candidates[i-1] and not self.visited[i-1]:
                continue
            self.visited[i] = True
            temp.append(candidates[i])
            self.helper(candidates, target, i+1, temp[:])
            self.visited[i]= False
            temp.pop()