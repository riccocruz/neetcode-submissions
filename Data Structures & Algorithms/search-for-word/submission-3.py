class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        visited = set()
        def backtrack(i, j, index):
            if index == len(word):
                return True
            if (
                0 <= i < M and \
                0 <= j < N and \
                (i, j) not in visited and \
                word[index] == board[i][j]
            ):
                visited.add((i, j))
                for x, y in DIRS:
                    if backtrack(i + x, j + y, index + 1):
                        return True
                visited.remove((i, j))
            return False
        
        for i in range(M):
            for j in range(N):
                if word[0] == board[i][j]:
                    visited = set()
                    if backtrack(i, j, 0):
                        return True
        return False