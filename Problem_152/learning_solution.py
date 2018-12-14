class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # temp = positive
        # positive = max(num, positive * num, negative * num)
        # negative = min(num, temp * num, negative * num)
        # 变量命名有点问题，positive指局部最大乘积（不一定是正数），negative指局部最小乘积（也不一定是负数）。
        positive, negative = nums[0], nums[0]
        result = nums[0]
        # print(result, positive, negative)
        for num in nums[1:]:
            positive, negative = max(num, positive * num, negative * num), min(num,
                                                                               positive * num, negative * num)         
            
            result = max(result, positive)
            # print(result, positive, negative)
        return result
            
        