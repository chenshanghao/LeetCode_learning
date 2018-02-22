class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while(left <= right):
            mid = left + (right - left) / 2
            print(mid)
            if nums[mid] == target:
                return mid
            elif (nums[left] <= nums[mid]):
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            elif (nums[left] > nums[mid]):
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1           
        return -1
                
            