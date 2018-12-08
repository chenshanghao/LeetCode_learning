# 在每一次插入过程中，其实只要把要插入的元素和倒数第二个元素进行比较，
# 如果相同，就忽略，因为倒数第一个数是夹在它们中间的，如果它们相等，那么就会有三个数相等；
# 如果不同，就可以插入，因为在这样的情况下，最多只有倒数第二、倒数第一两个数相等

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if count < 2 or nums[count - 2] != nums[i]:
                nums[count] = nums[i]
                count += 1
        return count