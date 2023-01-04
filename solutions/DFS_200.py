 class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(curr_i, curr_j):
            visited.add((curr_i, curr_j))
            for delta_i, delta_j in [(1,0), (-1,0), (0,1), (0,-1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == "1":
                    if (next_i, next_j) not in visited:
                        dfs(next_i, next_j)
        
        cnt = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:   #注意这里是（i，j）not in visited
                    dfs(i, j)
                    cnt += 1
        return cnt
