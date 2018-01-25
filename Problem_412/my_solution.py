class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a, b, c = "Fizz", "Buzz", "FizzBuzz"
        result = []
        num = 1
        while(n >= num):
            if num % 15 == 0:
                result.append(c)
            elif num % 3 == 0:
                result.append(a)
            elif num % 5 == 0:
                result.append(b)
            else:
                result.append(str(num))
            num += 1
        return result
        