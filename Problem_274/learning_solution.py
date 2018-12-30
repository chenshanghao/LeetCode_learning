class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations,reverse = True)
        i = 0
        while(i < len(citations)):
            if citations[i] < i+1: break
            i += 1
        return i

            
        