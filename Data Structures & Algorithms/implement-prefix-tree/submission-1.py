class PrefixTree:

    def __init__(self):
        self.trie = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.trie:
                cur.trie[c] = PrefixTree()
            cur = cur.trie[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.trie:
                return False
            cur = cur.trie[c]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.trie:
                return False
            cur = cur.trie[c]
        return True
        