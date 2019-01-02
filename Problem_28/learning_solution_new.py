class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        i = 0
        needleLength = len(needle)

        while i<len(haystack):
            a = haystack[i:i+needleLength]
            if a == needle:
                return i
            else:
                index = 0
                try:
                    # str.rindex(str, beg=0 end=len(string))
                    index = needle.rindex(haystack[i+needleLength])
                    i += needleLength - index
                except Exception:
                    i += needleLength + 1
        return -1
