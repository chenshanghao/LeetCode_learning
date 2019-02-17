class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        if n <=2: return max(nums)
        
        temp = [0] * n
        temp[0], temp[1] = 0, nums[1]
        
        temp_1 = [0] * n
        temp_1[0], temp_1[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2,n-1):
            temp[i] = max(temp[i-1], temp[i-2] + nums[i])
            temp_1[i] = max(temp_1[i-1], temp_1[i-2] + nums[i])
            
        temp[n-1] = max(temp[n-2], temp[n-3] + nums[n-1])
        temp_1[n-1] = temp_1[n-2]
        
        # print('temp:', temp)
        # print('temp_1:', temp_1)
        return max([temp[n-1], temp_1[n-1]])
        
        
        