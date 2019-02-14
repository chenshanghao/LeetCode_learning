class Solution:
    def restoreIpAddresses(self, s: 'str') -> 'List[str]':
    # @param s, a string
    # @return a list of strings
        if len(s) < 4 or len(s) > 12:
            return []
        self.result = []
        self.backtrack(s, 0, [])
        return self.result

    def backtrack(self, s, start, temp):
        if len(temp) == 4 and start == len(s):
            self.result.append(".".join(temp))
        for i in range(start, min(start + 4, len(s))):
            string = s[start: i + 1]
            if self.isValid(string):
                temp.append(string)
                self.backtrack(s, i + 1, temp)
                temp.pop()

    def isValid(self, string):
        if not string:  return False
        if len(string) > 1 and string[0] == '0':
            return False
        return int(string) <= 255
            
            
        