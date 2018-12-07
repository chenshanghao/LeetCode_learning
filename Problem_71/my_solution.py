class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = []
        path_split = path.split('/')
        for value in path_split:
            if value == '' or value == '.':
                continue
            elif value == '..':
                if len(res) > 0:
                    res.pop()
            else:
                res.append(value)
        
        ans = ''
        for value in res:
            ans += '/'
            ans += value 
        
        if ans == '':
            ans += '/'
        return ans
        