class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, n = len(s), 0

        if i == 0:
            return True
        elif i % 2 == 1:
            print("return")
        stack = []
        while(n < i):
            if s[n] == ')' or s[n] ==']' or s[n] =='}':
                if len(stack) == 0:
                    return False
                elif (s[n] == ')' and stack.pop() == '('):
                    n += 1
                elif (s[n] == ']' and stack.pop() == '['):
                    n += 1
                elif (s[n] == '}' and stack.pop() == '{'):
                    n += 1
                else:
                    return False
            else:
                stack.append(s[n])
                n += 1
        print(stack)
        if len(stack) == 0:
            return True
        else:
            return False