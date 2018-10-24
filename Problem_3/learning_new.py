class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Edge
        if not s:
            return 0

        start, max_length, hash = 0, 0, {}

        for index, value in enumerate(s):
            # Need to have the following condition:
            # start <= hash[num] to avoid edge case such as :
            # "tmmzuxt"
            if value in hash and start <= hash[value]:
                #update pointer
                start = hash[value] + 1
            else:
                max_length = max(max_length, index - start + 1)

            hash[value] = index

        return max_length