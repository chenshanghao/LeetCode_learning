class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        combine = x^y
        ans = 0
        while(combine > 0):
            if combine % 2 == 1:
                ans+=1
            combine/=2
        return ans