class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # step 1: change the array of edges representation to adjacency list
        graph = collections.defaultdict(list)    # list stores (neighbor, edge color)
        for u, v in redEdges:
            graph[u].append((v, "RED"))
        for u, v in blueEdges:
            graph[u].append((v, "BLUE"))
            
        # step 2: traversal the graph and update the res, we want to find the shortest steps, so use bfs
        res = [-1 for _ in range(n)]
        q = collections.deque()
        visited = set()
        q.append((0, "ORIGIN"))
        visited.add((0, "ORIGIN"))   # visiting the same node with same color is not allowed, with same color is not
        step = -1
        while len(q) > 0:
            step += 1
            lens = len(q)
            for _ in range(lens):
                curr_node, curr_color = q.popleft()
                if res[curr_node] == -1: 
                    res[curr_node] = step      # update res
                for next_node, next_color in graph[curr_node]:
                    if (next_node, next_color) in visited:  # visiting the same node with same color is not allowed
                        continue
                    if next_color == curr_color:    # have to alternate color
                        continue
                    q.append((next_node, next_color))
                    visited.add((next_node, next_color))
                    
        return res 
