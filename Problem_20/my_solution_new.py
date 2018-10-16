class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n%2 == 1:
            return False
        stack = []
        for i in range(n):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                tail = stack.pop()
                if (s[i] == ')' and tail == '(') or (s[i] == ']' and tail == '[') or (s[i] == '}' and tail == '{'):
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
            
        