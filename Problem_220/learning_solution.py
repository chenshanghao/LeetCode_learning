# 桶的方法 O(n)

# 思想是以t+1为间隔来分桶，对于一个数，将其分到第key = num / (t + 1) 个桶中，我们只需要查找相同的和相邻的桶的元素就可以判断有无重复。

# 比如t = 4，那么0~4为桶0，5~9为桶1，10~14为桶2 。

# 使用t+1个桶是为啥？这是为了避免除以0的错误，可能t = 0.


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False

        dic = collections.OrderedDict()

        for i in range(len(nums)):
            key = nums[i] / max(1, t)

            for m in (key, key - 1, key + 1):
                if m in dic and abs(nums[i] - dic[m]) <= t:
                    return True

            dic[key] = nums[i]

            if i >= k:
                dic.popitem(last = False)

        return False 
