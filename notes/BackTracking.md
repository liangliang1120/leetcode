### [78. Subsets](https://github.com/liangliang1120/leetcode/blob/main/solutions/78Subsets.py)
- number of subsets: 2^n, 2 to the power of n,but we need the subsets themself *n here, because each length of res need time
- 2 conditions: 1. add the nums[i], 2.not add
- tip: res.append(subset.copy)
- when the index i to n:  add res and resturn
- method2:
- res.append(subset.copy());for i in range(start, n): subset.add,backtrack(i+1),subset.pop
- Time: O(n(2^n)), Space:O(n)

### [90. Subsets II](https://github.com/liangliang1120/leetcode/blob/main/solutions/90-Subsets-II.py)
- sort()
- res.append(subset.copy());for i in range(start, n): if i> start and nums[i]==nums[i-1]:continue, subset.add,backtrack(i+1),subset.pop
- Time: O(n(2^n)), Space:O(n)

### [39. Combination Sum](https://github.com/liangliang1120/leetcode/blob/main/solutions/39-Combination-Sum.py)
- nums.sort()
- backtrack: 
- - if sum(subset) > target: return; 
- - if sum(subset) == target: res.append(subset)
- - for index in range(begin,n): 
- - - if sum(subset)+nums[index > target: break; 
- - - [subset.append(nums(index);backtrack(index);subset.pop()].   !!!backtrack(index)!!!----->unlimited number of times!!!
- Time: up to O(n(2^n)), Space:O(target) - recursive stack
- - n(2^n): each num can be put into subset, each subset put into res needs O(n)

### [40. Combination Sum II](https://github.com/liangliang1120/leetcode/blob/main/solutions/40-Combination-Sum-II.py)
- nums.sort()
- backtrack: 
- - if sum(subset) > target: return; 
- - if sum(subset) == target: res.append(subset)
- - for index in range(begin,n): 
- - - if sum(subset)+nums[index > target: break; 
- - - if index > begin and nums[index] == nums[index-1]: continue
- - - [subset.append(nums(index);backtrack(index+1);subset.pop()]
- Time: up to O(n(2^n)),O(S), S is the length of the solution; Space:O(target)

### [46. Permutations](https://github.com/liangliang1120/leetcode/blob/main/solutions/46-Permutations.py)
- use visited, index, subset, res, n = len(nums)
- if len(subset) == n: res.append(subset.copy())
- for i in range(n): if not visited, update(visited),subset.append(nums[i]),backtrack(), update(visited)
- Time: O(n * n!), Space:O(n)

### [47. Permutations II](https://github.com/liangliang1120/leetcode/blob/main/solutions/47-Permutations-II.py)
- use visited, index, subset, res, n = len(nums)
- nums.sort()
- if len(subset) == n: res.append(subset.copy())
- for i in range(n): 
- - if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]: continue
- - if not visited, update(visited),subset.append(nums[i]),backtrack(), update(visited)
- Time: O(n * n!), Space:O(n)

### [79. Word Search](https://github.com/liangliang1120/leetcode/blob/main/solutions/79-Word-Search.py)
- directions,height,witdth,visited=set()
- for i,j in positions, check
- def check(i,j,k):
- - if board[i][j] != word[k]: false
- - if k == n - 1: true
- - visited.add((i,j)), 
- - for di,dj in directions:0<=ni<h...!!!if (ni.nj) not in visited and check(ni,nj,k+1):return true
- - visited.remove(i,j)
- Time: O(M*N*(3^L),M and N:height & width,L is the length of word. each time go to 3 directions
- Space:O(M*N), for visited

### [131. Palindrome Partitioning](https://github.com/liangliang1120/leetcode/blob/main/solutions/131-Palindrome-Partitioning.py)
- res, part, n = len(s),dfs
- def isPalidrome: 2 pointers
- dfs:
- - if i >= n: res.append(part.copy),return
- - for j in range(i,n): if isPali(s,i,j): part.append,dfs(j+1),part.pop --> if s[i:j] isPali, add in part, then dfs(next),pop for different s[i:j] situation to get next
- Time: O(n * 2^n), n is the length of s; Space:O(n^2), for the part=[], O(n) for stack,each stack O(n) space


### [17. Letter Combinations of a Phone Number](https://github.com/liangliang1120/leetcode/blob/main/solutions/17-Letter-Combinations-of-a-Phone-Number.py)
- backtrack(i) from index 0 to len(digits)
- phoneMap[digits[index]]
- Time: O(3^m * 4^n), m:the num corresponding to 3chars; n:the num corresponding to 4chars 
- Space:O(m+n): for recursion










