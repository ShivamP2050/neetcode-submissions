class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        first = word[0]
        visited = set()

        def dfs(i, j, num) -> bool:
            if num >= len(word):
                return True
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or (i, j) in visited:
                return False
            if board[i][j] == word[num]:
                visited.add((i, j))
                res =  (dfs(i + 1, j, num + 1) or
                 dfs(i - 1, j, num + 1) or
                 dfs(i, j + 1, num + 1) or
                 dfs(i, j - 1, num + 1))
            else:
                return False
            visited.remove((i, j))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == first:
                    if dfs(i, j, 0) == True:
                        return True

        return False


        