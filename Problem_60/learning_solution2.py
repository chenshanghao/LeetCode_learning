import math

class Solution:
    def getPermutation(self, n, k):
        res = [0] * n
        numbers = [x for x in range(1, n + 1)]
        k = k - 1
        fact = 1
        for i in range(2,n):
            fact *= i
        i = 0
        while i < n:

            index = k // fact
            res[i] = numbers[index]  # 确定一位数字
            numbers.pop(index)  # 使用过的数字，将不再使用
            
            # 更新 k
            k = k % fact  # 或者 k = k % fact
            if n-i-1 > 0:
                fact = fact//(n-i-1)
            i += 1
        return ''.join([str(x) for x in res])
    
# 现在总结规律：
# （1）第k个数字的第1位数字一定为[1, 2, ... n][k // (n-1)!]。

# 解释： 很显然，所有排列一共有n*(n-1)!种，也可以理解为，每个数字开头的种类组合有(n-1)!个。所以k // (n-1)!就可以算出第一位数字，5 // (3-1)! = 2，所以[1, 2, ... ... n][2] = 3 ，即，求出第一位数字了。

# （2）现在已经确定了第1位数字了，接下来要用同样的方法求解第2位上的数字。但要注意两点：

# 1、已经使用过的数字，将不再使用。

# 2、k值的更新，这个过程其实就是确定一位数字之后，进一步确定在新的范围内是第几个数字。
