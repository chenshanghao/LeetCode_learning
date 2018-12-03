class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        # 因为n个不同的数字可以组成n!个序列，那么首位确定的序列都有(n-1)!种不同的可能性，
        # 而且这些序列都根据首位的大小进行了分组，1...是最小的(n-1)!个，2...是(n-1)!+1到2(n-1)!个，
        # 那么现在只需要计算k中有几个(n-1)!就可以确定首位的数字，同样可以通过这样的方法来确定第二位、第三位……
        # 此外，由于列表下标从0开始，所以k要减去1。
        k -= 1
        factorial = 1
        for i in range(1, n):
            factorial *= i
        
        result = []
        array = list(range(1, n+1))
        print(k, factorial)
        for i in range(n-1, 0, -1):
            index = k // factorial
            result.append(str(array[index]))
            array = array[:index] + array[index+1:]
            k %= factorial
            factorial //= i
            print(k, factorial)
        result.append(str(array[0]))
        
        return "".join(result)