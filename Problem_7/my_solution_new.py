class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #attention 1
        # 忘记最后的check
        result = 0
        if x==0 or x>(pow(2,31)-1) or x<(-pow(2,31)):
            return result
        flag=1 if x>0 else -1
        x = abs(x)
        while(x!=0):
            tail=x%10
            x=x/10
            result = result*10 + tail
        result = result*flag
        if result>(pow(2,31)-1) or result<(-pow(2,31)):
            return 0
        return result
        