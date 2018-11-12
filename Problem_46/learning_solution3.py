class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.backtrack(nums, [])
        return self.result

    def backtrack(self, nums, temp):
        # print(temp)
        if len(temp) == len(nums):
            self.result.append(temp[:])
                # 由于长度一样, 所以不用知道 index,连 i 都免了
        else:
            for n in nums:
                if n in temp:
                    continue
                temp.append(n)
                self.backtrack(nums, temp)
                temp.pop()
        