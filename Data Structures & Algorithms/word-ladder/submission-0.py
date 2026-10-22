from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj = defaultdict(list)
        for word in wordList:
            for j in range(len(wordList)):
                pattern = word[:j] + "*" + word[j + 1:]
                adj[pattern].append(word)
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for adj_word in adj[pattern]:
                        if adj_word not in visit:
                            visit.add(adj_word)
                            q.append(adj_word)
            
            res += 1
        
        return 0

                