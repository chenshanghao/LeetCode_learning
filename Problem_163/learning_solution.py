class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        start = lower-1
        res = []
        for i in range(len(nums)+1):
            if i==len(nums):
                end=upper+1
            else:
                end = nums[i]
            
            if end-start >= 2:
                res.append(self.range(start+1, end-1))
            
            start=end
        return res
    
    def range(self, l, r):
        if l == r:
            return str(l)
        else:
            return str(l) + '->' + str(r)
            
            
