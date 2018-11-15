class DFS:
    def subsets(self, S):
        self.result = []
        self.backtrack(0, sorted(S), [])
        return self.result

    def backtrack(self, start, S, temp):
        self.result.append(temp[:])
        for i in range(start, len(S)):
            temp.append(S[i])
            self.backtrack(i+1, S, temp)
            temp.pop()