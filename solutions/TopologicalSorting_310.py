class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        inDegree = collections.defaultdict(int)
        neighbors = collections.defaultdict(list)
        for u,v in edges:
            inDegree[u] += 1
            inDegree[v] += 1
            neighbors[u].append(v)
            neighbors[v].append(u)

        q = collections.deque()
        for node, indg in inDegree.items():
            if indg == 1:
                q.append(node)

        centers = []
        while q:
            size = len(q)
            centers = []
            for _ in range(size):
                curr = q.popleft()
                centers.append(curr)
                for next_node in neighbors[curr]:
                    inDegree[next_node] -= 1
                    if inDegree[next_node] == 1:
                        q.append(next_node)
        return centers
