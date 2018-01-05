class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return None
        elif len(nums) == 3:
            return sum(nums)
        
        result = nums[0] + nums[1] + nums[2]
        diff = abs(result - target)
        
        # 排序nlogn
        nums.sort()
        
        for index, a in enumerate(nums):
            if index >= 1 and nums[index - 1] == a:
                continue
            left, right = index + 1, len(nums) - 1
            
            while(left < right): 
                sum_abc = a + nums[left] + nums[right]
                diff_abc = abs(sum_abc - target)
                if diff_abc < diff:
                    diff = diff_abc
                    result = sum_abc
                if(sum_abc - target < 0):
                    left += 1
                elif(sum_abc - target > 0):
                    right -= 1
                elif(sum_abc - target == 0):
                    return target
        return result

def execute():
    sol = Solution()
    print(sol.threeSumClosest([1,1,1,1], 0))
        