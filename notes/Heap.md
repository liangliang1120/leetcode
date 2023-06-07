- 见到数组要想到先排序.
- 见到集合求Min/max 就用堆
- 见到需要维护一个集合的最小值/最大值的时候要想到用堆.
- 第k小的元素，Heap用来维护当前候选集合.
- 
- heappush(heap,n)数据堆入，最小堆
- heappop(heap)将数组堆中的最小元素弹出
- heapify(heap) 将heap属性强制应用到任意一个列表
- heapreplace(heap，n)弹出最小的元素被n替代
- nlargest(n,iter)、nsmallest(n,iter)
- Return a list with the n largest elements from the dataset defined by iterable.Equivalent to: sorted(iterable, key=key, reverse=True)[:n].

### [703. Kth Largest Element in a Stream](https://github.com/liangliang1120/leetcode/blob/main/solutions/703-Kth-Largest-Element-in-a-Stream.py)
- heapq.heapify(self.queue)
- heapq.heappush(self.queue, val)
- heapq.heappop(self.queue)
- heap from small to big
- keep k length of the queue, push into, pop out
- time:O(nlogk) 只维护前k个O(nlogk) for initialize, logk for insert
- space: O(k), 只维护k个的话O(k)

### [1046. Last Stone Weight](https://github.com/liangliang1120/leetcode/blob/main/solutions/1046-Last-Stone-Weight.py)
- heapify(stone)
- x, y = heapq.heappop(stones)
- if x - y > 0: heapq.heappush(stones, temp)
- return -stones[0] if len(stones) == 1 else 0
- time:O(nlogn) get a number from heap is O(logn),get n - 1 times
- space: O(n)

### [973. K Closest Points to Origin](https://github.com/liangliang1120/leetcode/blob/main/solutions/973-K-Closest-Points-to-Origin.py)
- 所有的距离加进heap， hp=[]， hp.append(), heapify(hq)
- while k>0:加前k个进res
- time:O(nlogk)维护前k个O(nlogk)
- space: O(k),维护k个的话O(k)

### [215. Kth Largest Element in an Array](https://github.com/liangliang1120/leetcode/blob/main/solutions/215-Kth-Largest-Element-in-an-Array.py)
- heapify and reverse
- time:O(nlogn) ,heapify is O(n), delete need O(klogn)
- space: O(logN)

### [621. Task Scheduler*](https://github.com/liangliang1120/leetcode/blob/main/solutions/621-Task-Scheduler.py)
- maxHeap for recording the count
- deque for the pairs of [-cnt, idleTime],cnt: left frequency of this kind of task, when can start this task 
- while q or maxHeap: 
- - time +1; 
- - if not maxHeap: time=q[0][1] else: if cnt q.append([cnt,time + n]) <-- cnt = heapq.heappop(maxHeap) + 1,cnt == 0 means no tasks any more
- - if q and q[0][1] == time: heapq.heappush(maxHeap,q.popleft()[0]) <-- if can start,q.pop,maxHeap.push
- time:O(n) ---> log26, add into, count each frequency
- space: O(n)

### [355. Design Twitter](https://github.com/liangliang1120/leetcode/blob/main/solutions/355-Design-Twitter.py)
- hashmap, linkedlist,heap

### 239. [Sliding Window Maximum](https://github.com/liangliang1120/leetcode/blob/main/solutions/Heap_239.py)
- (负数，idx)加进q，先只加k个进去，heapify.  
- 然后用heap维护window，加进push一个，
- ans初始化-q[0][0],right_pointer从k开始向右走，heapq.heappush(q, (负数，idx))，
- while idx <= i-k,heappop弹出更大且idx在前面的,只剩下windows内的最大值
- 每次循环ans加q中windows内的最大的
- time O(nlogn) space O(n)

### 912. [Sort an Array](https://github.com/liangliang1120/leetcode/blob/main/solutions/Heap_912.py)

### 253. [Meeting Rooms II](https://github.com/liangliang1120/leetcode/blob/main/solutions/Heap_253.py)
- 先排序 key = lambda x: x[0]
- 最早结束的时间加进q   heapq.heappush(free_rooms, intervals[0][1])
- 从第二个开始遍历，if开始时间 晚于 上一个结束时间:pop-heapq.heappop(free_rooms)。加当前的结束时间。
- 返回heap内的个数-即房间数




