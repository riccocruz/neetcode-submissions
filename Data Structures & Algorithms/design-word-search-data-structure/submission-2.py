class WordDictionary:

    def __init__(self):
        self.trie = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.trie:
                cur.trie[c] = WordDictionary()
            cur = cur.trie[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(i, cur):
            if i == len(word):
                return cur.is_end
            
            if word[i] != '.' and word[i] not in cur.trie:
                return False
            
            if word[i] == '.':
                for c in cur.trie:
                    if dfs(i + 1, cur.trie[c]):
                        return True
                return False
            
            return dfs(i + 1, cur.trie[word[i]])

        return dfs(0, self)