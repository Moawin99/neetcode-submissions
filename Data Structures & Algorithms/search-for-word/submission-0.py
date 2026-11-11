class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def trav(r, c, i, board):
            if i == len(word):
                return True
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i] or (r,c) in path):
                return False
            
            path.add((r,c))
            res = (trav(r- 1, c, i + 1, board) or
            trav(r, c- 1, i + 1, board) or
            trav(r, c + 1, i + 1, board) or
            trav(r + 1, c, i + 1, board))
            path.remove((r,c))
            return res
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if trav(i, j, 0, board):
                    return True
        
        return False