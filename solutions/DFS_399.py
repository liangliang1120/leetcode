class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(curr_node, end, curr_div):
            visited.add(curr_node)
            if curr_node == end:
                self.div = curr_div   #can not directly append to res, bcz if we donot find it we need append -1
                return
            for next_node, div in graph[curr_node]:
                if next_node not in visited:
                    next_div = div * curr_div
                    dfs(next_node, end, next_div)
        
        graph = defaultdict(list)
        for i, (u, v) in enumerate(equations):
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))
        
        mutiple = 1
        
        res = []
        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1.0)
                continue
            if start == end:
                res.append(1.0)
                continue
            self.div = -1   #record each time div
            visited = set()  #每一次都要重新记录哪些点是否被访问
            dfs(start, end, 1)
            res.append(self.div)
        return res
