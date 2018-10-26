class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maximum_list = nums[0:k]
        k_max = min(maximum_list)
        # print('k_max: ', k_max)
        for i in range(k, len(nums)):
            if nums[i] > k_max:
                for j in range(len(maximum_list)):
                    if maximum_list[j] == k_max:
                        maximum_list[j] = nums[i]
                        break
                k_max = min(maximum_list)
            # print('maximum_list: ', maximum_list)
            # print('k_max: ', k_max)
        return k_max
        