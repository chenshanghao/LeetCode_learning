class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        """
        0----->         0                                               2n-2
        1----->         1                                       2n-3    2n-1
        2----->         2                               2n-4            2n
        3----->         3                       2n-5                    2n+1
        4----->         4                   .                           .
        5----->         .           n+1                                 .
        6----->         n-2     n                                       3n-2
        n-1----->       n-1                                             3n-3
        
        cycle = 2*n-2
        result =""
        row = 0
        x = 0
        row i:
            zig = cycle * x + i
            zag = cycle * (x+1) -i
        row 0 and n-1 ---------> there is no zag

        if n == 1 ------> return x
        """
        result = ''
        length = len(s)
        n = numRows
        cycle = 2 * n -2
        if n == 1:
            return s

        i = 0
        x = 0
        while len(result) < length:
            if cycle * x + i > length -1:
                i += 1
                x = 0
            zig = cycle * x + i
            zag = cycle *(x+1) - i
            if i ==0 or i == n-1:
                result += s[zig]
            else:
                if zag > length -1:
                    result += s[zig]
                else:
                    result += s[zig] + s[zag]
            x += 1
        return result

def execute():
    sol = Solution()
    print(sol.convert("PAHNAPLSIIGYIR", 4))

if __name__ == "__main__":
    execute()
