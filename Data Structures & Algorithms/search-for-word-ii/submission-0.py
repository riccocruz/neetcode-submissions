class Trie:
    def __init__(self):
        self.trie = {}
        self.is_end = False
    
    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.trie:
                cur.trie[c] = Trie()
            cur = cur.trie[c]
        cur.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        M, N = len(board), len(board[0])
        DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = []

        word_trie = Trie()
        visited = set()
        for word in words:
            word_trie.add_word(word)

        def dfs(i, j, cur_trie, cur_word):
            if (
                0 <= i < M and \
                0 <= j < N and \
                (i, j) not in visited and \
                board[i][j] in cur_trie.trie
            ):
                visited.add((i, j))
                cur_trie = cur_trie.trie[board[i][j]]
                cur_word += board[i][j]
                if cur_trie.is_end:
                    res.append(cur_word)
                    cur_trie.is_end = False

                for x, y in DIRS:
                    dfs(i + x, j + y, cur_trie, cur_word)
                visited.remove((i, j))



        for i in range(M):
            for j in range(N):
                if board[i][j] in word_trie.trie:
                    visited = set()
                    dfs(i, j, word_trie, "")
        return res