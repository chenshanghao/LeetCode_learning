class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_key_nums= {}
        for i in nums:
            if i in dict_key_nums:
                dict_key_nums[i] += 1
            else:
                dict_key_nums[i] = 1
        results = []
        for i in range(k):
            max_key, max_value = 0, 0
            for k,v in dict_key_nums.items():
                if v > max_value:
                    max_key, max_value = k, v
            results.append(max_key)
            del dict_key_nums[max_key]
        return results
            