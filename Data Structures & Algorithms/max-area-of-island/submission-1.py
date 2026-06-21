class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        res = 0
        
        def dfs(i, j):
            if (i < 0 or j < 0 or j == cols or i == rows or grid[i][j] == 0
            or (i, j) in visit):
                return 0
            visit.add((i, j))
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
                   

        for i in range(rows):
            for j in range(cols):
                res = max(dfs(i, j), res)
        return res



        