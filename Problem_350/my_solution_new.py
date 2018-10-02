class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #1. What if the given array is already sorted? How would you optimize your algorithm?
        # 用two pointers 比较？

        #2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
        # 将nums1 的数据存进hash map，然后遍历nums2 查找是否在nums1中？ 时间复杂度不变，但是节省空间
        
        #3. What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into               the memory at once?

        # 因为nums1是可以放到内存的，所以就把nums1放到hashmap里，然后从disk分多次取出nums2，判断一下就好了


        
        dict_nums1 = {}
        ans = []
        for i in nums1:
            if i in dict_nums1:
                dict_nums1[i] += 1
            else:
                dict_nums1[i] = 1
                
        for i in nums2:
            if (i in dict_nums1) and (dict_nums1[i]>0):
                ans.append(i)
                dict_nums1[i] -= 1
        return ans
        
        
        
        
        
        
#         此方法创建两个dict,两次遍历        
#         dict_nums1, dict_nums2 = {}, {}
#         ans = []
#         for i in nums1:
#             if i in dict_nums1:
#                 dict_nums1[i] += 1
#             else:
#                 dict_nums1[i] = 1
        
#         for i in nums2:
#             if i in dict_nums2:
#                 dict_nums2[i] += 1
#             else:
#                 dict_nums2[i] = 1
        
#         for key,value in dict_nums1.items():
#             if key in dict_nums2:
#                 num = min(dict_nums1[key], dict_nums2[key])
#                 ans = ans +[key]*num
#         return ans
            
        