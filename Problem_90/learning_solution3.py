class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.helper(sorted(nums), 0, [])
        return self.result
        
    def helper(self, s, start, tmp):
        self.result.append(tmp[:])
        for i in range(start, len(s)):
            if i>start and s[i] == s[i-1]:
                continue
            tmp.append(s[i])
            self.helper(s, i+1, tmp)
            tmp.pop()
        