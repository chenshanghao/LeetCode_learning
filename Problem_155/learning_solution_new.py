class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_len = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.stack_len += 1

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.stack_len -= 1
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()