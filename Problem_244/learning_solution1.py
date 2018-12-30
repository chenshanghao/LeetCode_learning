class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.dic = {}
        for index, value in enumerate(words): # key/value 对是 值/index索引list
            if value not in self.dic:
                self.dic[value] = [index]
            else:
                self.dic[value] += index,

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return min(abs(x-y) for x in self.dic[word1] for y in self.dic[word2])