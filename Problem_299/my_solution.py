class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n = len(secret)
        if n == 0:
            return "0A0B"
        
        bull = 0
        secret_dict, guess_dict ={}, {}
        for i in range(n):
            if secret[i] == guess[i]:
                bull += 1
            else:
                if secret[i] in secret_dict:
                    secret_dict[secret[i]] += 1
                else:
                    secret_dict[secret[i]] = 1
                
                if guess[i] in guess_dict:
                    guess_dict[guess[i]] += 1
                else:
                    guess_dict[guess[i]] = 1
        cow = 0
        for key in secret_dict:
            if key in guess_dict:
                cow = cow + min(secret_dict[key], guess_dict[key])
                
        return str(bull) + 'A' + str(cow) + 'B'
                    