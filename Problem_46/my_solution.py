class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.backtrack(nums,[])
        return self.result
    
    def backtrack(self, S, temp):
        if len(temp) == len(S):
            self.result.append(temp[:])   
        for i in range(len(S)):
            if S[i] in temp:
                continue
            temp.append(S[i])
            self.backtrack(S, temp)
            temp.pop()
        
        
    