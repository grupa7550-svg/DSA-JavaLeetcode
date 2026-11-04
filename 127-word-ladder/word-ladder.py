from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue
                    nxt = word[:i] + c + word[i + 1:]
                    if nxt in words and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))
        return 0