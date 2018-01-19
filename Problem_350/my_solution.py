class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict_nums1, dict_nums2 = self.build_dict(nums1), self.build_dict(nums2)
        results = []

        for i in dict_nums1:
            if i in dict_nums2:
                j = min(dict_nums1[i], dict_nums2[i])
                while( j > 0):
                    results.append(i)
                    j -= 1
        return results
        
    
    def build_dict(self, nums):
        dict_nums = {}
        for i in nums:
            if i in dict_nums:
                dict_nums[i] += 1
            else:
                dict_nums[i] = 1
        return dict_nums