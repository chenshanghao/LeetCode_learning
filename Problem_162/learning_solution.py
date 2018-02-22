#float('inf')   max_integer
#float('-inf')  -max_integer
#首先我们找到中间节点mid，如果大于两边返回当前index就可以了，如果左边的节点比mid大，那么我们可以继续在左半区间查找，这里面一定存在一个peak，为什么这么说呢？假设此时的区间范围为[0, mid - 1]， 因为num[mid - 1]一定大于num[mid]了，如果num[mid - 2] <= num[mid - 1]，那么num[mid - 1]就是一个peak。如果num[mid - 2] > num[mid - 1]，那么我们就继续在[0, mid - 2]区间查找，因为num[-1]为负无穷，所以最终我们绝对能在左半区间找到一个peak。同理右半区间一样。


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        start, end = 0 , n-1
        while(start <= end):
            mid = start + (end - start) / 2
            if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == n-1 or nums[mid] > nums[mid+1]):
                return mid
            elif(mid > 0 and nums[mid - 1] > nums[mid]):
                end = mid - 1
            else:
                start = mid + 1
        return mid
        