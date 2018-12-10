class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        # wordList.append(endWord)
        curr_list = [beginWord]
        depth = 1
        while(curr_list != []):
            new_list=[]
            for words in curr_list:
                if words == endWord:
                    return depth
                for i in range(len(words)):
                    for alphabet in alphabets:
                        if (words[0:i] + alphabet + words[i+1:]) in wordList:
                            new_word = words[0:i] + alphabet + words[i+1:]
                            new_list.append(new_word)
                            wordList.remove(new_word)
            curr_list = new_list
            depth+=1
        return 0