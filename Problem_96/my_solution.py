class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [1, 1]
        for i in range(2, n+1):
            temp = 0
            for j in range(1, i+1):
                temp += a[j-1] * a[i-j]
            a.append(temp)
        return a[n]
        