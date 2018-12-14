class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op_list = ['+', '-', '*','/']
        stack = []
        for value in tokens:
            if value in op_list:
                right = stack.pop()
                left = stack.pop()
                if value == '+':
                    stack.append(left+right)
                elif value == '-':
                    stack.append(left-right)
                elif value == '*':
                    stack.append(left*right)
                else:
                    stack.append(int(left/right))
            else:
                stack.append(int(value))
        return stack[0]
                
        