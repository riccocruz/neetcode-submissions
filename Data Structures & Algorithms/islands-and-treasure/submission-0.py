class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        stack = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    stack.append([i, j])

        while stack:
            curr = []
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            print(stack)
            for x, y in stack:
                for a, b in dirs:
                    if (
                        0 <= x + a < m and \
                        0 <= y + b < n and \
                        grid[x + a][y + b] not in (0, -1) and \
                        grid[x + a][y + b] > grid[x][y]
                    ):
                        grid[x + a][y + b] = grid[x][y] + 1
                        curr.append(([x + a, y + b]))
            stack = curr
