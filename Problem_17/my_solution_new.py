digits_dict ={
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}
        

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        if len(digits) == 0:
            return ans
        ans = []
        return self.__letterCombinations(ans, digits)
            
    def __letterCombinations(self, ans, digits):
        if len(digits) > 1:
            ans = self.__letterCombinations(ans, digits[:len(digits)-1])
        new_ans = []
        if len(ans) > 0:
            for word in digits_dict[digits[-1]]:
                for string in ans:
                    new_ans.append(string+word)
        else:
            for word in digits_dict[digits[0]]:
                new_ans.append(word)
            
        ans = new_ans
        return ans
            
            