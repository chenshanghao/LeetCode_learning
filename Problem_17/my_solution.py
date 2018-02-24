dict_digits = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
            
        }
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        length = len(digits)
        result = []
        if length == 0:
            return result
        self.dfs(length, 0, '', digits, result)
        return result
    
    def dfs(self, length, num, string, digits, result):
        if len(string) == length:
            result.append(string)
            return
        for letter in dict_digits[digits[num]]:
            self.dfs(length, num+1, string+letter, digits, result)