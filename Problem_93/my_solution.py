class Solution:
    def restoreIpAddresses(self, s: 'str') -> 'List[str]':
        result = []
        if len(s) < 4 or len(s)>16:
            return result
        self.helper(s, 0, 0, '', result)
        return result
    
    def helper(self, s, start, num, tmp, result):
        if num >= 4:
            return
        
        for i in range(start+1, start+4):
            if s[start] == '0' and i>start+1:
                    return
            if i<len(s) and int(s[start:i]) < 256:
                new_tmp = tmp[:] + (s[start:i] + '.')
                self.helper(s, i, num+1, new_tmp,result)
            
            if i==len(s):
                if num == 3 and int(s[start:i]) < 256:
                    result.append(tmp[:] + s[start:i])
                return
            
            if i>len(s):
                return
            
            
            
        