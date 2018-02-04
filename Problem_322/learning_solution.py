# 本参考程序来自九章算法，由 @Jay 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param: coins: a list of integer
    @param: amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        if not coins or not amount:
            return 0
        m, n = amount + 1, len(coins)
        P = [m for _ in range(m)]
        P[0] = 0

        for total in range(m):
            for deno in range(n):
                if coins[deno] <= total \
                        and P[total - coins[deno]] + 1 < P[total]:
                    P[total] = P[total - coins[deno]] + 1

        # since the init value of each child in `P` is `m == amount + 1`
        # so if `P[amount] > amount` means it not changed -> not valid
        return -1 if P[amount] > amount else P[amount]