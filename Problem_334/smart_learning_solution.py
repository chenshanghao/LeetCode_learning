import sys
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False

        limit=sys.maxint
        mins=nums[0]
        i=1
        while i<len(nums):
            if nums[i]>limit:
                return True
            if nums[i]>mins:
                limit=min(nums[i],limit)
            mins=min(mins,nums[i])
            i+=1
    
    return False