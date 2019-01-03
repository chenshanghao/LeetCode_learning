class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        i = 0
        ch = list(s)
        j = len(s)-1
       
        while i<j:
            # replace
            if ch[i] in vowels and ch[j] in vowels:
                t = ch[i]
                ch[i] = ch[j]
                ch[j] = t
                j-=1
                i+=1
            # advance
            if not ch[i] in vowels:
                i+=1
            if not ch[j] in vowels:
                j-=1
            
        return "".join(ch)