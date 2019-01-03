class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        if m != n:
            return False
        corr_dict = {}
        for index,sub_str in enumerate(s):
            if (sub_str in corr_dict) and (t[index] != corr_dict[sub_str]):
                return False
            
            if sub_str not in corr_dict:
                if t[index] in corr_dict.values(): return False
                else:   corr_dict[sub_str] = t[index]
        return True
        