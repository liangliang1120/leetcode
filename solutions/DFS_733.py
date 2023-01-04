class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(curr_i, curr_j):
            visited.add((curr_i, curr_j))
            image[curr_i][curr_j] = color

            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and image[next_i][next_j] == start_color:
                    if (next_i, next_j) not in visited:
                        dfs(next_i, next_j)     

        m, n = len(image), len(image[0])            
        visited = set()
        start_color = image[sr][sc]
        dfs(sr, sc)
        return image
