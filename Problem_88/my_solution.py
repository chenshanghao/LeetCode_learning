class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
            
        i, j = m - 1, n - 1
        for k in range(m + n - 1, -1, -1):
            if i < 0 or j < 0:
                break
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

                
        if i < 0:
            for k in range(j, -1, -1):
                nums1[k] = nums2[k]

        