class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(1,k+1):
                if i+j >= len(nums):
                    break
                if abs(nums[i] - nums[i+j]) <= t:
                    return True
        return False
        