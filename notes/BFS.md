```
while q:
  cur = q.pop()
  for node in cur.neighbors:
    if node.isvalid and node not in visited:
      q.push(node)
```
记录层序level：
```
q = collections.deque([root])
level = 0
while q:
  size = len(q)
  while size--:
    cur = q.pop()
    for node in cur.neighbors:
      if 【node.isvalid】 and node not in visited:
        q.append(node)
   level += 1
```
# 🌲的BFS

### 102. [Binary Tree Level Order Traversal](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_102.py)
bfs 记录层序框架 node isvalid,判断左右子节点

### 103. [Binary Tree Zigzag Level Order Traversal](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_103.py)
同102, bfs 记录层序框架 res append的时候注意层次

### 104. [Maximum Depth of Binary Tree](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_104.py)
bsf 记录层序框架：while (纵向) res每层+1 for(横向，迭代每个queue中的元素）验证存在子节点：queue.append
time: O(n), space: worst O(n)

### 107. [Binary Tree Level Order Traversal II](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_107.py)
同102, bfs 记录层序框架 返回[::-1]

### 111. [Minimum Depth of Binary Tree](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_111.py)
bsf 记录层序框架, 如果not left and not right: return level

### 199. [Binary Tree Right Side View](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_199.py)
同102, bfs 记录层序框架 for循环结束后 res不是加所有元素，只加最右边一个

### 314. [Binary Tree Vertical Order Traversal](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_314.py)
层序遍历，每次加进q两个元素（node，index),用defaultdict存储，最后[res[x] for x in sorted(res.keys())]
defaultdict(list)

### 513. [Find Bottom Left Tree Value](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_513.py)
同102, bfs 记录层序框架, 返回最后一层第一个

### 662. [Maximum Width of Binary Tree](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_662.py)
同102, bfs 记录层序框架, 每次加进q的时候,cur = q.popleft,index= cur[1],左节点加进的时候(cur[0].left, index*2),右节点加进的时候(cur[0].roght, index*2)
同一层记录第一个index和最后一个，相减，与全局变量对比

### 637. [Average of Levels in Binary Tree](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_637.py)

### 1161. [Maximum Level Sum of a Binary Tree](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_1161.py)
bfs 记录层序框架，中间记录最大的和及对应层数

# 图
### 997. [Find the Town Judge](https://github.com/liangliang1120/leetcode/blob/main/solutions/Graph_997)
- trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi
- for loop trust, 每次bi入度+1, ai出度-1
- 法官入度=n-1，出度=0
- 建图
```
   n_degree = defaultdict(int)
        out_degree = defaultdict(int)
        for u, v in trust:
            in_degree[v] += 1
            out_degree[u] -= 1
```

### 277. [Find the Celebrity](https://github.com/liangliang1120/leetcode/blob/main/solutions/Graph_277)
- 循环1，先找出一个candidate 他不认识除了0之外的所有人
- 循环2，如果不是自己的话，candidate认识别人 或 有人不认识candidate，就返回-1； 否则 返回candidate



# 图的BFS
### 261. [Graph Valid Tree](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_Graph_261)
- 先判断一下：edge number = node number - 1
- 建图，无向图用a dictionary of adjacency node,key是节点，value是相邻的节点
- BFS 直接遍历框架，图比树多了一个visited set(),bfs作用是遍历所有节点，
- 最后判断遍历后，viited里面的数量，是否都遍历到了 len(visited) = n

### 133. [Clone Graph](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_133)
- 用BFS找所有nodes
- 建新nodes存到mapping 
- 复制nodes和neighbors

### 323. [Number of Connected Components in an Undirected Graph](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_323.py)
- visited set,graph ajacency dict双向存储
- 对每个节点循环，bfs用来遍历，每次遍历完了res+1

# 矩阵的BFS
### 200. [Number of Islands](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_200)
- for循环，一旦是1，BFS遍历把所有是1的改成0，cnt+1

### 994. [Rotting Oranges](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_994)
- 先遍历一遍，如果是腐烂的橘子：位置加入q，起始可能有多个初始值在q里；如果是新鲜橘子：记录数量fresh
- BFS记录level的框架，每层res+1, while条件加上fresh数量大于0

### 286. [Walls and Gates](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_286)
- BFS记录层序的框架
- 先把遍历把gate加进q，每层逐个赋值level
- 如果被访问过，已经赋值为最短距离，就不是2147483647了，只有=2147483647的才赋值level和加进q

### 1730. [Shortest Path to Get Food](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_1730)
- BFS记录level的框架，如果遇到食物，就返回level
- 注意，visited和q同时更新

### 1162. [As Far from Land as Possible](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_1162.py)
- 水先加进q，BFS层序遍历框架，返回最后的level
- 注意visited和q同时更新

### 542. [01 Matrix](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_542)
- BFS层序遍历框架
- 注意visited和q同时更新

# 需要自己定义next节点的BFS
### 127. [Word Ladder](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_127.py)
- 当前word换了一个char，就算作当前基因的next节点
- Time: O(N*C^2) N:word个数，C:average word length
- Space: O(N*C^2)

### 397. [Integer Replacement](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_397.py)
- 求the minimum number of operation needed 带层序的BFS
- next 节点两种情况：除以2 或者 curr+1/curr-1

### 433. [Minimum Genetic Mutation](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_433)
- 当前基因换了一个character并且在bank_set里面，就算作当前基因的next节点

### 752. [Open the Lock](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_752.py)
- 求最小次数 带层序的BFS
- 轮转-1 +1再对10取模

### 1197. [Minimum Knight Moves](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_1197.py)
- 8个方向是next node
- 到了目标点就返回level
- time: O(N^2) space:O(N^2)

### 1129. [Shortest Path with Alternating Colors](https://github.com/liangliang1120/leetcode/blob/main/solutions/BFS_1129.py)
- the shortest path from node 0 to node x -> BFS
- 要先建图,无向图，adjacency list，双向加颜色

# 拓扑排序 Topological Sorting
- 构建有向图，inDegree = collections.defaultdict(int) key是node, val是这个node的indegree值
- 如果inDegree == 0，就加进初始化的q
- 用BFS模板，拿到一个node就inDegree-1，==0的时候加进res
```python
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here

        # 1. collect indgree information of each node an store in a dict
        in_degree = collections.defaultdict(int)
        for node in graph:
            if node not in in_degree:
                in_degree[node] = 0
            for n in node.neighbors:
                in_degree[n] += 1

        #2. topological sorting -bfs
        q = collections.deque()
        for node in graph:
            if in_degree[node] == 0:
                q.append(node)
        res = []        
        while q:
            curr = q.popleft()
            res.append(curr)
            for next_node in curr.neighbors:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    q.append(next_node)
        return res
```

### 207. [Course Schedule](https://github.com/liangliang1120/leetcode/blob/main/solutions/TopologicalSorting_207.py)
- 建图，为了后面bfs遍历时找neighbor node
- in degree都设置为0，再遍历根据prerequisites赋值好indegree
- 用bfs拓扑排序：初始化indegree==0加进初始化q
- 出q时加进res，每次遍历到就indegree-1

### 210. [Course Schedule II](https://github.com/liangliang1120/leetcode/blob/main/solutions/TopologicalSorting_210.py)
- 思路同上，如果len(res)==numCourses,return res
- Time: O(n+m)每个节点减去其prerequisites才遍历完 
- Space:O(n+m), adjacent list: O(n+m); q:O(n)
- n:number of courses,m:prerequisite
           
### 310. [Minimum Height Trees](https://github.com/liangliang1120/leetcode/blob/main/solutions/TopologicalSorting_310.py)
- 最小高度树，最小，BFS从外面向中心遍历
- 无向图，in_degeree双向+1，neighbors建图也双向
- 初始化q加进indegree==1的点
- BFS求centers所有符合的中心点，有层序的bfs，因为最后一层才是结果
- 每层都把取出来的curr节点放进centers更新，对neighbors每个节点indegree-1操作，只有indegree==1才加进q
- 类似拓扑排序。最后一层的所有nodes就是根节点


