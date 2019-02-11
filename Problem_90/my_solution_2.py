class Solution:
    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        self.result = []
        self.helper(0, sorted(nums), [])
        return self.result
    
    def helper(self, start, S, temp):
        if temp in self.result:
            return
        self.result.append(temp[:])
        for i in range(start, len(S)):
            temp.append(S[i])
            self.helper(i+1,S,temp)
            temp.pop()
        
        