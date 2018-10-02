class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        int_put_result, out_put_result = '0', '1'

        while(n > 1):
            n -= 1
            int_put_result = out_put_result
            out_put_result = ""
            value = "-1"
            start, end = -1, -1
            for i in range(len(int_put_result)):
                if value != int_put_result[i]:
                    if start == -1:
                        start, value = i, int_put_result[i]
                    else:
                        end = i - 1
                        length = (end - start + 1)
                        out_put_result += str(length) + value
                        start, end, value = i, -1, int_put_result[i]
            
            out_put_result += str(len(int_put_result) - start) + str(value) 
            
        return out_put_result
                    
        
        