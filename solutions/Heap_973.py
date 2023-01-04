#排序
import heapq
import random


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:k]
    
#heap    
'''
这个是n个都heapify
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []
        for i, point in enumerate(points):    
            x, y = point[0], point[1]
            hq.append((x*x+y*y, i))
        
        heapify(hq)
        
        res = []
        while k > 0:          # 取前k个
            res.append(points[heappop(hq)[1]])
            k -= 1
        return res
    
'''
堆 - 只维护k个
time O(nlogk) 其中 n 是数组 points 的长度。
由于大根堆维护的是前 k 个距离最小的点，因此弹出和插入操作的单次时间复杂度均为 O(logk)。

space O(logk)
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:k])]
        heapq.heapify(q)
        
        n = len(points)
        for i in range(k, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            heapq.heappushpop(q, (dist, i))
        
        ans = [points[identity] for (_, identity) in q]
        return ans


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dis(x):
            return x[0]**2 + x[1]**2

        return heapq.nsmallest(k, points,key = dis)   
    
