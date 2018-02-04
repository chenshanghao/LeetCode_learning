class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums <= 1:
            return len_nums
        results = []
        for index,i in enumerate(nums):
            result = 1
            for j in range(index+1):
                if nums[j] < i:
                    result = max(results[j] + 1, result)
            results.append(result)
        return max(results)
                
        
        