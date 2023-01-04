class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mark_walk = set() # 标记走过的路
        path_dict = {}

        for i in range(n):
            path_dict[i] = []

        for i in edges:
            path_dict[i[0]].append(i[1])
            path_dict[i[1]].append(i[0])

        def bfs(root):
            if root in mark_walk or root not in path_dict: return 
            mark_walk.add(root)

            for i in path_dict[root]:
                bfs(i)
        
        ans = 0
        for i in range(2001):
            if i not in mark_walk and i in path_dict:
                ans += 1
                bfs(i)

        return ans
