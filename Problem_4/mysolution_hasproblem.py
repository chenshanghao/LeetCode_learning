class Solution(object):

	def findMedianSortedArray(self, nums):
		len_nums = len(nums)
		if len_nums % 2 == 0:
			return (nums[len_nums/2] + nums[len_nums/2-1])/2.0
		else:
			return nums[len_nums/2]/1.0

	def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0:
        	return	findMedianSortedArray(nums2)
        if len(nums2) == 0:
        	return	findMedianSortedArray(nums1)


        if len(nums1) > len(nums2):
        	nums1, nums2 = nums1, nums2

        x,y = len(nums1), len(nums2)
        low, high = 0, x
        while(x <= high):
        	partitionX = (low + high)/2
        	partitionY = (x+y+1)/2 - partitionX

        	# if partitionX is 0 it means nothing is there on left side, 
        	# if partitionY is length of input then there is nothing on the right side.

        	maxLeftX = nums1[partitionX - 1] if partitionX!=0 else  -9223372036854775808
        	minRightX = nums1[partitionX] if partitionX != x else  9223372036854775807

        	maxLeftY = nums2[partitionY - 1] if partitionY!=0 else -9223372036854775808
        	minRightY = nums2[partitionY] if partitionY!=y else 9223372036854775807

        	if (maxLeftX <= minRightY and maxLeftY <= minRightX):
        		if(x + y) %2 == 0:
        			return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2.0
        		else:
        			return max(maxLeftX,maxLeftY)/1.0
        	elif maxLeftX > minRightY:
        		high = partitionX - 1
        	else:
        		low = partitionX + 1





        # len_nums1, len_nums2 = len(nums1), len(nums2)
        # start_nums1, end_num1 = 0, len(nums1)-1
        # start_nums2, end_num2 = 0, len(nums2)-1
        # total_len = len(nums1) + len(nums2)

        # if len_nums1 == 0:
        # 	if len_nums2 % 2 == 0:
        # 		return (nums2[len_nums2/2] + nums2[len_nums2/2-1])/2.0
        # 	else:
        # 		return nums2[len_nums2/2]
        # if len_nums2 == 0:
        # 	if len_nums1 % 2 == 0:
        # 		return (nums1[len_nums1/2] + nums1[len_nums1/2-1])/2.0
        # 	else:
        # 		return nums1[len_nums1/2]

        # if total_len %2 == 0:
        # 	while (start_nums1 + start_nums2 + 1) *2 < total_len:
        # 		if nums1[start_nums1]> nums2[start_nums2]:
        # 			start_nums2 = (start_nums2 + end_num2)//2 + 1
        # 		else:
        # 			start_nums1 = (start_nums1 + end_num1)//2 + 1
        # 	total = nums1[start_nums1]
        # 	return (nums1[start_nums1] + nums2[start_nums2]) / 2
        # else:
        # 	while  (start_nums1 + start_nums2 + 2) *2 < total_len:
        # 		if nums1[start_nums1]> nums2[start_nums2]:
        # 			start_nums2 = (start_nums2 + end_num2)//2 + 1
        # 		else:
        # 			start_nums1 = (start_nums1 + end_num1)//2 + 1
        # 	if nums1[start_nums1] > nums2[start_nums2]:
        # 		return nums1[start_nums1]/1.0
        # 	else:
        # 		return nums2[start_nums2]/1.0

        