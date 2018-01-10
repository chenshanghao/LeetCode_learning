class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # write your code here
        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]
        num3 = [0 for _ in range(len(num1)+ len(num2))]
        
        # 这一块要学习,好方法
        for i in range(len(num1)):
            for j in range(len(num2)):
                num3[i+j] += int(num1[i]) * int(num2[j])
        
        for i in range(len(num3)):
            if num3[i] > 9:
                num3[i + 1] += num3[i] // 10
                num3[i] %= 10
        res = ''.join(str(n) for n in num3[::-1])        
            
        return str(int(res))