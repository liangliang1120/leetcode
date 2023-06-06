class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        h,w = len(board),len(board[0])
        visited = set()
        n = len(word)
        def check(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == n - 1:
                return True
            visited.add((i,j))
            # res = False
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w:
                    if (ni, nj) not in visited:
                        if check(ni, nj, k + 1):
                            return True
            visited.remove((i,j))
            return False

        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        return False
