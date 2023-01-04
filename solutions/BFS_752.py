class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target in deadends:
            return -1
        
        q = collections.deque()
        visited = set()
        q.append("0000")
        visited.add("0000")
        
        layer = -1
        while len(q) > 0:
            size = len(q)
            layer += 1
            for _ in range(size):
                curr = q.popleft()
                if curr == target:
                    return layer
                if curr in deadends:
                    continue
                for next_str in self.getNext(curr):
                    if next_str not in visited:
                        q.append(next_str)
                        visited.add(next_str)
        return -1
    
    def getNext(self, curr):
        res = []
        for i in range(len(curr)):
            curr_num = int(curr[i])
            for delta in [-1, 1]:
                next_num = (curr_num + delta) % 10
                next_node = curr[:i] + str(next_num) + curr[i+1:]
                res.append(next_node)
        return res
