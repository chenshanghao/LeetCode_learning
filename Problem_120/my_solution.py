class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        a = [triangle[0][0]]
        for i in range(1, len(triangle)):
            temp = []
            for j in range(len(triangle[i])):
                min_step = triangle[i][j]
                if j == 0:
                    temp.append(min_step + a[j])
                elif j == len(triangle[i]) - 1:
                    temp.append(min_step + a[j-1])
                else:
                    temp.append(min_step + min(a[j-1], a[j]))
            a = temp
            # print(a)
        return min(a)
                    
                
        