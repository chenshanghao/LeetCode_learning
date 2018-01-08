class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        len_n = len(A)
        if len_n < 1:
            return 0
        dict_num1, dict_num2 = {}, {}
        results = 0
        
        "A+B dict"
        for i in range(len_n):
            for j in range(len_n):
                new_sum =  A[i] + B[j]
                if new_sum in dict_num1:
                    dict_num1[new_sum] += 1
                else:
                    dict_num1[new_sum] = 1
        "C+D dict"
        for i in range(len_n):
            for j in range(len_n):
                new_sum =  C[i] + D[j]
                if new_sum in dict_num2:
                    dict_num2[new_sum] += 1
                else:
                    dict_num2[new_sum] = 1
        
        for key in dict_num1.iterkeys():
            if -key in dict_num2:
                results += dict_num1[key] * dict_num2[-key]
        
        return results
            
                
        
        
        
                        
                
        