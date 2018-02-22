class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums) - 1
        start, end = 0, n
        result = []
        while(start <= end):
            mid = start + (end - start) / 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if start > end:
            return [-1, -1]
        else:
            i, j = mid, mid
            while(i>=0 and nums[i] == target ):
                i -= 1
            while(j <= n and nums[j] == target):
                j += 1
            return [i + 1, j - 1]
            
        