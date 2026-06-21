import queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [0, 1], [-1, 0], [0, -1]]
        time = 0
        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        while q and fresh > 0:

            for i in range(len(q)):
                dr, dc = q.popleft()
                for r, c in DIRECTIONS:
                    nr = dr + r
                    nc = dc + c
                    if (nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == 1):
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            time += 1

        if fresh == 0:
            return time
        else:
            return -1

            