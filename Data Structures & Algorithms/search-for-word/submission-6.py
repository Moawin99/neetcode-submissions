class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visited = [[False for _ in range(COL)] for _ in range(ROW)]


        def dfs(i, r, c, visited):
            if i == len(word):
                return True
            if min(r, c) < 0 or r >= ROW or c >= COL or visited[r][c] or word[i] != board[r][c]:
                return False

            visited[r][c] = True
            res = (dfs(i + 1, r + 1, c, visited) or
                    dfs(i + 1, r - 1, c, visited) or    
                   dfs(i + 1, r, c + 1, visited) or
                   dfs(i + 1, r, c - 1, visited))
            visited[r][c] = False
            
            return res

        for i in range(ROW):
            for j in range(COL):
                if dfs(0, i, j, visited):
                    return True
        return False