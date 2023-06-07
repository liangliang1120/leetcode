class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-c for c in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            temp = x - y
            if temp < 0:
                heapq.heappush(stones, temp)
        return -stones[0] if len(stones) == 1 else 0
