class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))

        length = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if (r,c) == (ROWS-1, COLS-1):
                    return length
    
                neighbors = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
                for row, col in neighbors:
                    if(0 <= row < ROWS and 0 <= col < COLS and 
                        grid[row][col] == 0 and (row,col) not in visit):

                        queue.append((row,col))
                        visit.add((row,col))
            length += 1
        return -1