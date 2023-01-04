class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        m,n = len(board),len(board[0])
        visited = set()
        
        def check(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i,j))
            result = False
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if (ni, nj) not in visited:
                        if check(ni, nj, k + 1):
                            return True
            visited.remove((i,j))
            return result
            
        
        for i in range(m):
            for j in range(n):
                if check(i,j,0):
                    return True
        return False        
        
        
