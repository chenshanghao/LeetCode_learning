class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.backtrack(0, sorted(nums), [])
        return self.result
    
    def backtrack(self, start, S, temp):
        self.result.append(temp[:])
        for i in range(start, len(S)):
            if i>start and S[i]==S[i-1]:
                continue
            temp.append(S[i])
            self.backtrack(i+1, S, temp)
            temp.pop()
        