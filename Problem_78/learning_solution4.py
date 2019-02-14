class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        self.result = []
        self.helper(sorted(nums), 0, [])
        return self.result
        
    def helper(self, s, start, tmp):
        self.result.append(tmp[:])
        for i in range(start,len(s)):
            tmp.append(s[i])
            self.helper(s, i+1, tmp)
            tmp.pop()
        