class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        if x == 0 or x < pow(-2,31) or x > pow(2,31) -1:
            return result
        flag = 1 if x>0 else -1
        x = abs(x)
        while(x != 0):
            tail = x % 10
            x = x // 10
            result = result*10 + tail
        result = result * flag
        if result < pow(-2, 31) or result > pow(2, 31) -1:
            return 0
        return result
    
        # 错误1: store integers within the 32-bit signed integer range: [−231,  231 − 1]  需要正反面考虑
        # 错误2: 负数(negative number)求余数方法不对
        