class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        num = [num for num in range(1,10)]
        if n-(k-1) <9:   num = num[:n-(k-1)]            
        self.backtrack(0, num, k, n, [])
        return self.result
    
    def backtrack(self,start, num, k, n, temp):
        if len(temp) > k:   return
        if sum(temp) > n:   return
        if sum(temp) == n and len(temp) == k:
            self.result.append(temp[:])
            
        for i in range(start, len(num)):
            temp.append(num[i])
            self.backtrack(i+1, num, k,n,temp)
            temp.pop()
    