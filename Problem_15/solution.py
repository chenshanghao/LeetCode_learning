class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort nlogn  --- quick sort, mergesort, Heapsort
        # n --- 基数排序, 桶排序(research)

        results = []
        nums.sort()
        for index, a in enumerate(nums):
            #若一位相等，去掉重复的
            if index >= 1 and nums[index-1] == a:
                continue 
            #给左边和右边赋值
            left, right = index + 1, len(nums) - 1
            while(left < right):
                b, c = nums[left], nums[right]
                total = a + b + c
                if total == 0:
                    results.append([a, b, c])
                    while(left < right and nums[left] == nums[left+1]):
                        left += 1
                    while(left<right and nums[right]==nums[right-1]):
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1

        return results

def execute():
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))

