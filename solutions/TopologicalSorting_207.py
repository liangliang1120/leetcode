class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        # graph - adjacency list
        graph = collections.defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)

        # indegree info of all the nodes
        inDegree = collections.defaultdict(int)
        for n in range(numCourses):
            inDegree[n] = 0
        for u,v in prerequisites:
            inDegree[u] += 1

        # topological sorting - bfs
        q = collections.deque()
        for node, i in inDegree.items():
            if i == 0:
                q.append(node)
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for next in graph[curr]:
                inDegree[next] -= 1
                if inDegree[next] == 0:
                    q.append(next)
        return len(res) == numCourses
