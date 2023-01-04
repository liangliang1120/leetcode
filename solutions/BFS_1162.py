class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        cnt0 = 0
        cnt1 = 1

        row, col = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    q.append((i, j))
                    visited.add((i, j))
                    cnt1 += 1
                if grid[i][j] == 0:
                    cnt0 += 1
        if cnt0 == 0 or cnt1 == 0:
            return -1
            
        level = -1
        while q:
            level += 1
            size = len(q)
            for _ in range(size):
                (x, y) = q.popleft()
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx, ny = x + dx, y + dy
                    if 0<= nx<row and 0 <= ny < col and (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx,ny))
                    # print(visited)
        return level
