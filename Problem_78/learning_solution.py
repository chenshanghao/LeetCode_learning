class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
            print(res)
        return res
       
# Your input
# [1,2,3]
# Your stdout
# [[], [1]]
# [[], [1], [2], [1, 2]]
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
