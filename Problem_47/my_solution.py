class Solution:
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        self.result = []
        self.visited = [False] * len(nums)
        self.helper(sorted(nums),[])
        return self.result
    
    def helper(self, nums, temp):
        if len(nums) == len(temp):
            self.result.append(temp[:])
        for index,value in enumerate(nums):
            if self.visited[index]: continue
            if index>0 and nums[index] == nums[index-1] and self.visited[index-1]:
                continue
            temp.append(value)
            self.visited[index] = True
            self.helper(nums, temp[:])
            self.visited[index] = False
            temp.pop()