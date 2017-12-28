class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        symbol = 1
        s=''
        
        if x < 0:
            symbol=-1
            s=str(-x)
        elif x==0:
            return 0
        else:
            symbol=1
            s=str(x)
        result = int(s[-1::-1]) * symbol
        
        # 学习一下
        if abs(result) > 0x7FFFFFFF:
            return 0
        else:
            return result
            
        
        
        