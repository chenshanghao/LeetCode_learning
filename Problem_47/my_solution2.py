class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        visit = [False] * len(nums)
        self.helper(sorted(nums), [], visit, result)
        
        return result
    
    def helper(self, s, tmp, visit, result):
        if len(tmp) == len(s):
            result.append(tmp[:])
        
        for i in range(0, len(s)):
            if visit[i]:
                continue
            if i>0 and s[i] == s[i-1] and visit[i-1]:
                continue
            tmp.append(s[i])
            visit[i]=True
            self.helper(s, tmp, visit, result)
            tmp.pop()
            visit[i]=False
        