class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        N,M = len(grid), len(grid[0])
        cache = [[0] * M for _ in range(N)]
        return self.dfs(0,0, grid, set(), N, M)

    def dfs(self, i, j, grid, cache, N, M):
        if (min(i,j) < 0 or i == N or j == M or (i,j) in cache or grid[i][j] == 1):
            return 0
        if i == N - 1 and j == M - 1:
            return 1

        cache.add((i,j))

        count = 0
        count += self.dfs(i + 1, j, grid, cache, N, M)
        count += self.dfs(i - 1, j, grid, cache, N, M)
        count += self.dfs(i, j + 1, grid, cache, N, M)
        count += self.dfs(i, j - 1, grid, cache, N, M)

        cache.remove((i,j))
        return count