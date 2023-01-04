class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        q = collections.deque()
        visited = set()
        q.append(beginWord)
        visited.add(beginWord)
        
        steps = 0
        while len(q) > 0:
            steps += 1
            lens = len(q)
            for _ in range(lens):
                curr_word = q.popleft()
                if curr_word == endWord:
                    return steps
                for next_word in self._get_next(word_set, curr_word):
                    if next_word not in visited:
                        q.append(next_word)
                        visited.add(next_word)
        return 0
    
    def _get_next(self, word_set, curr_word):
        res = []
        for i, ch in enumerate(curr_word):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                if letter == ch:
                    continue
                next_word = curr_word[:i] + letter + curr_word[i+1:]
                if next_word in word_set:
                    res.append(next_word)
        return res
