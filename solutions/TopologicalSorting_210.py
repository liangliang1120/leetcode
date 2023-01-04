class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = collections.defaultdict(list)
        for u,v in prerequisites:
            G[v].append(u)

        inDegree = collections.defaultdict(int)
        for n in range(numCourses):
            inDegree[n] = 0
        for u,v in prerequisites:
            inDegree[u] += 1
        
        q = collections.deque()
        for node,i in inDegree.items():
            if i == 0:
                q.append(node)

        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for next_node in G[curr]:
                inDegree[next_node] -= 1
                if inDegree[next_node] == 0:
                    q.append(next_node)
        # print(res)
        if len(res) == numCourses:
            return res

        return []

