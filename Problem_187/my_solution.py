class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        ret = []
        if n <= 10:
            return ret
        dna_dict = {}
        for i in range(n-9):
            if s[i:i+10] not in dna_dict:
                dna_dict[s[i:i+10]] = 1
            else:
                dna_dict[s[i:i+10]] += 1
            
            if dna_dict[s[i:i+10]] == 2:
                ret.append(s[i:i+10])
        
        return ret
                
        
        