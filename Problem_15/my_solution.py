class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        ans_list = []
        i = 0
        while(i<(n-2)):
            while(i>=1 and nums[i] == nums[i-1] and i<(n-2)):
                i += 1
            if i >= (n-2):
                break
            j = i+1
            k = n-1
            while(j < k):
                if nums[i] + nums[j] + nums[k] == 0:
                    ans_list.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while((nums[j-1] == nums[j]) and (j<k)):
                        j+=1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                    while((nums[j-1] == nums[j]) and (j<k)):
                        j+=1
                else:
                    k-=1
                    while((nums[k+1] == nums[k]) and (j>k)):
                        k-=1
            i+=1
        return ans_list
            
            