class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        
        dict_value = {}
        for i in range(len(nums)):
            if nums[i] in dict_value:
                dict_value[nums[i]].append(i)
            else:
                dict_value[nums[i]] = [i]
        for key in dict_value:
            if len(dict_value[key]) > 1:
                for i in range(len(dict_value[key])):
                    for j in range(i+1, len(dict_value[key])):
                        if abs(dict_value[key][i] - dict_value[key][j]) <= k:
                            return True
            
        return False
            
        
        