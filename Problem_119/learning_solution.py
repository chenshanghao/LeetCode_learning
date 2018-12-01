class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res_list = [1]
        for i in range(1,rowIndex+1):
            new_list = [1]
            for index in range(0, len(res_list)-1):
                new_list.append(res_list[index] + res_list[index+1])
            new_list.append(1)
            res_list = new_list
        return res_list
        