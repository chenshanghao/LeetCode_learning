class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.vistor = [False] * len(nums)
        self.backtrack(sorted(nums), [])
        return self.result
    
    def backtrack(self, S, temp):
        if len(temp) == len(S):
            self.result.append(temp[:])
        else:
            for i in range(len(S)):
                if self.vistor[i]: continue
                if i>0 and S[i] == S[i-1] and self.vistor[i - 1]:
                    continue
                self.vistor[i] = True
                temp.append(S[i])
                self.backtrack(S, temp)
                self.vistor[i] = False
                temp.pop()
        
        