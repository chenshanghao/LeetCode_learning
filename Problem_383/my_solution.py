class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        al_dict = {}
        for s in magazine:
            if s not in al_dict:
                al_dict[s] = 1
            else:
                al_dict[s] += 1
        for s in ransomNote:
            if s in al_dict and al_dict[s] >= 1:
                al_dict[s] -= 1
            else:
                return False
        return True
        