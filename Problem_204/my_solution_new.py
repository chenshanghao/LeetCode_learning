class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n < 2:
        #     return 0
        # Attention: less than
        ans = [0] * n
        for i in range(2, n):
            if ans[i] == 1:
                continue
            else:
                num = i + i
                while(num < n):  #这里出错了
                    ans[num] = 1
                    num += i
        result_num = 0 
        for i in range(2, n):
            if ans[i] == 0:
                result_num += 1
        return result_num