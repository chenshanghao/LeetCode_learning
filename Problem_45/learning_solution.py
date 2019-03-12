class Solution:
    def jump(self, nums: List[int]) -> int:
        last_max_reach, current_max_reach = 0 , 0
        njump , i = 0 , 0
        while current_max_reach < len(nums)-1:
            while i <= last_max_reach:
                current_max_reach = max(i+nums[i],current_max_reach)
                i+=1
            if last_max_reach == current_max_reach:
                return -1
            last_max_reach = current_max_reach
            njump+=1
        return njump

        