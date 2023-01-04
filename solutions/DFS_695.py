class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [(0,1), (0,-1),(-1,0),(1,0)]
        n = len(grid)
        m = len(grid[0])
        visited = set()      

        def dfs(x, y):
            maxA = 1
            visited.add((x,y))
            for delta_i, delta_j in dir:
                next_i = x + delta_i
                next_j = y + delta_j
                if 0 <= next_i < n \
                and 0 <= next_j < m \
                and grid[next_i][next_j] == 1 \
                and (next_i,next_j) not in visited:
                    maxA += dfs(next_i, next_j) 
            return maxA

        maxA = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    maxA = max(maxA, dfs(i, j))
        return maxA

    
    
class Solution:
    def __init__(self):
        self.maxArea = 0
        self.area = 1
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[-1, 0],[1, 0],[0,-1],[0,1]]
        def dfs(grid, i, j):
            if grid[i][j] == 0:
                # 已经是海水了
                return 
            
            grid[i][j] = 0
            m = len(grid)
            n = len(grid[0])
            
            for d in dirs:
                next_i = i + d[0]
                next_j = j + d[1]
                if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == 1:
                    # print(i,j,next_i,next_j)
                    self.area += 1
                    dfs(grid, next_i, next_j)
       
        
        m = len(grid)
        n = len(grid[0])
            
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    # res += 1
                    self.area = 1
                    dfs(grid, i ,j)
                    if self.area > self.maxArea:
                        self.maxArea = self.area

        return self.maxArea
