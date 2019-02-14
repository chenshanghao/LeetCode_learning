digit2letters = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
    }
class Solution:
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        result = []
        if not digits:
            return []

        self.helper(digits, "", 0, result)
        return result
    
    def helper(self, digits, tmp, start, result):
        if len(tmp) == len(digits):
            result.append(tmp)
            return
            
        for i in digit2letters[digits[start]]:
            new_tmp = tmp[:] + i
            self.helper(digits, new_tmp, start+1, result)