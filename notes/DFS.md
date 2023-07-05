```python
def dfs(curr):
  visited.add(curr)
  for next in curr.neighbors:
    if next not in visited:
      dfs(next)
```
## 使用场景
- 排列，组合
- 找出所有的情况

# 普通DFS
### 339. [Nested List Weight Sum](https://github.com/liangliang1120/leetcode/blob/main/solutions/DFS_339.py)
- self.sum
- dfs (list, depth)

### 399. [Evaluate Division](https://github.com/liangliang1120/leetcode/blob/main/solutions/DFS_399.py)
- 无向图，adacency list graph.append((v,values[i]) graph.append((u,1/values[i])
- 每次都要记录visited，重新计算self.div, append res
- dfs(start, end, div)

### 841. [Keys and Rooms](https://github.com/liangliang1120/leetcode/blob/main/solutions/DFS_399.py)
- start from 0, get into dfs
- use visited to record 
- time O(n+m) n:rooms num. m:total num of keys
- space: O(n) stack

### 1236. [Web Crawler](https://github.com/liangliang1120/leetcode/blob/main/solutions/DFS_1236.py)
- dfs 中间判断是否同一个domain（split）
- htmlParser.getUrls(currUrl)获取next节点
- dfs(startUrl)


# 矩阵DFS
### 200 [Number of Islands](https://github.com/liangliang1120/leetcode/blob/main/solutions/DFS_200.py)
两个for循环grid中所有的点,如果是“1”，res+1,进入dfs把所有相邻的1都设为0
dfs注意点：如果是0，直接返回；i 在外面循环的时候对应n,那么dfs中也检查0<=next_i<n;如果在范围内，且=1，继续dfs

### 695. [Max Area of Island](https://github.com/liangliang1120/leetcode/blob/main/solutions/DFS_695.py)
- (x,y) not in visited
- 外部：maxA = 0,  maxA = max(maxA, dfs(i, j))
- 每次dfs过程中 maxA = 1. maxA += dfs(next_i, next_j) 

### 733. [Flood Fill](https://github.com/liangliang1120/leetcode/blob/main/solutions/DFS_733.py)
- 所有相邻的颜色都变

# 🌲DFS
## 104 [Maxmum depth of binary tree](https://github.com/liangliang1120/leetcode/blob/main/solutions/DFS_104.py)
- if not root: 0; left_d=dfs(root.left); right_d=dfs(root.right);return max(left_d, right_d) + 1
- Time: O(N)
- DFS Space:O(height), BFS Space: worest case O(n)

## 124. [Binary Tree Maximum Path Sum](https://github.com/liangliang1120/leetcode/blob/main/solutions/DFS_124.py)
- self.res = float("-inf")
- def max_sum_oneside(node):return max(0, max(left_s, right_s) + node.val)
- self.res = max(self.res, left_s + right_s + node.val)
- time: O(n), space: O(height)(栈空间：递归深度）
## 110. [Balanced Binary Tree](https://github.com/liangliang1120/leetcode/blob/main/solutions/DFS_124.py)
- dfs递归求height，当前树的高度=max(左子树高度，右子树高度)+1。heigt_diff判断，并且递归左右子树判断
- max(height(root.left), height(root.right)) + 1


## [94 binary tree inorder traversal](https://github.com/liangliang1120/leetcode/blob/main/solutions/0094-Binary-Tree-Inorder-Traversal.py)
list dfs(root,res): root ==null:return , dfs(root.left,res), res.add(val), dfs(root.right, res)

## [543. Diameter of Binary Tree](https://github.com/liangliang1120/leetcode/blob/main/solutions/0543-Diameter-of-Binary-Tree.py)
- 全局变量 self.d 
- dfs(root): if not root: 0; 左半径left_d=dfs(root.left); 右半径right_d=dfs(root.right); 更新直径self.d = max(self.d, left_d +right_d+1); return 半径max(left_d, right_d) + 1
- return self.d - 1
- time: O(n), space: O(height)(栈空间：递归深度）


## [110. Balanced Binary Tree](https://github.com/liangliang1120/leetcode/blob/main/solutions/0110-Balanced-Binary-Tree.py)
- the same method as 104 for depth -> diff depth
- abs(height_diff) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

## [100. Same Tree](https://github.com/liangliang1120/leetcode/blob/main/solutions/0100-Same-Tree.py)
- return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

## [572. Subtree of Another Tree](https://github.com/liangliang1120/leetcode/blob/main/solutions/0572-Subtree-of-Another-Tree.py)
- return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
- isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

  
# BackTrack
- DFS vs Backtrack 不同: Backtrack有剪枝，DFS是暴力，Backtrack是在暴力法上的优化
- 问题类型：  1.求所有路径。  2.combination/permutation 组合/排列。

```python   
初始化进入
def backtrack(candidate):    # 递归的定义很重要    
   if find_solution(candidate):   
      output(candidate)    # normally a deep copy for list  
      return    
   for next_candidate in list_of_candidates:    # iterate all possible next candidates.  
      if is_not_valid(next_candidate):    # In the above example: “N” != “I”  
       continue  
     place(next_candidate)        # try this partial candidate solution        
     backtrack(next_candidate)    # given the candidate, explore further.      
     remove(next_candidate)       # backtrack      
  
```
```python   
空进入
def backtrack(candidate):    # 递归的定义很重要 
   if is_not_valid(candidate):   
       return 

   place(next_candidate)        # try this partial candidate solution 
   
   if find_solution(candidate):   
       output(candidate)    # normally a deep copy for list  
       return  
   else:
       for next_candidate in list_of_candidates:    # iterate all possible next candidates.  
          backtrack(next_candidate)    # given the candidate, explore further.      
   
   remove(next_candidate)       # backtrack      
  
```
套用模板:  
如果允许一个数取多次：则next candidate从 i 开始. 
如果不允许一个数取多次：则next candidate从 i+1 开始 (subsets). 
如果不允许一个数取多次且输入有重复元素题目要求去重：则分两步，第一步sort, 第二步去重判断，且next candidate从 i+1 开始. 
如果(1, 3)和(3, 1)认为是不同答案(premutation)：则不需要start_idx, for loop每次都从零开始就可以了，但是每个数只能取一次，所以需要一个visited set做标记.  

在写代码之前一定要先写下三点： 
- 什么是backtrack的结束条件   
- next_candidate有哪些constraint   
- 将什么传入backtrack函数   


### 17. [Letter Combinations of a Phone Number](https://github.com/liangliang1120/leetcode/blob/main/solutions/DFS_17.py)
- hashmap{2:abc,3:def...
- 回溯，backtrack(0) 长度没有到len(input)的时候，取键盘上的字母for: temp.append(); backtarck（index+1); temp.pop()
- time O(3^n*4^m) space:O(m+n)只与递归深度有关

### 113. [Path Sum II](https://github.com/liangliang1120/leetcode/blob/main/solutions/DFS_113.py)
dfs回溯。res和path都可以用全局变量，不用传入dfs函数。注意：path.append,path.pop; res加path的时候要加path[:] or path.copy()
- return all root-to-leaf path  -> backtrack

### 79. [Word Search](https://github.com/liangliang1120/leetcode/blob/main/solutions/DFS_113.py)
- visited标记已经走过的，backtrack
- backtrack(i,j,word_idx) idx = target长度 - 1：返回true

### 784. [Letter Case Permutation](https://github.com/liangliang1120/leetcode/blob/main/solutions/DFS_784.py)
- -1进入dfs
- time:O(n*2^N) 递归深度n，所有递归子状态2^n
- space:O(n*2^N)



