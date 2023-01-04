class Solution:
    def integerReplacement(self, n: int) -> int:
        q = collections.deque([n])
        visited = set()
        visited.add(n)
        layer = -1
        while q:
            layer += 1
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == 1:
                    return layer
                if curr % 2 == 0:
                    next_num = curr /2
                    if next_num not in visited:
                        q.append(next_num)
                        visited.add(next_num)
                else:
                    for next_num in [curr -1, curr +1]:
                        if next_num not in visited:
                            q.append(next_num)
                            visited.add(next_num)
