class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        self.result = []
        self.helper(nums, [])
        return self.result
    
    def helper(self, nums, temp):
        if len(temp) == len(nums):
            self.result.append(temp[:])
            return
        for i in nums:
            if i not in temp:
                temp.append(i)
                self.helper(nums, temp[:])
                temp.pop()
            