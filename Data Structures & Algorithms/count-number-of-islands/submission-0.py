class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        count = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            while queue:
                row, col = queue.popleft()
                grid[row][col] = "0"
                for nr, nc in directions:
                    cr, cc = row + nr, col + nc
                    if cr >= 0 and cc >= 0 and cr < len(grid) and cc < len(grid[0]) and grid[cr][cc] == "1":
                        queue.append((cr, cc))



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        return count
                    

                

        