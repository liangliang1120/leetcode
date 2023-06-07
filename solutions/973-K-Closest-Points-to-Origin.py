class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = [[ -x*x - y*y, i] for i, (x,y) in enumerate(points[0:k])]
        heapq.heapify(queue)
        for i in range(k, len(points)):
            x, y = points[i]
            dist =  -x*x - y*y
            heapq.heappush(queue, [dist, i])
            heapq.heappop(queue)
        
        return [points[i] for dist,i in queue]
