class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_value_index = {}
        for index, value in enumerate(numbers):
            if target-value in dict_value_index:
                return [dict_value_index[target-value] + 1, index + 1]
            else:
                dict_value_index[value] = index