class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1, n+1):
            if i%5 ==0 and i%3 == 0:
                ans.append("FizzBuzz")
            elif i%5 == 0:
                ans.append("Buzz")
            elif i%3 == 0:
                ans.append("Fizz")
            else:
                ans.append(str(i))
        return ans