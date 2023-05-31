### [78. Subsets](https://github.com/liangliang1120/leetcode/blob/main/solutions/78Subsets.py)
- number of subsets: 2^n, 2 to the power of n,but we need the subsets themself *n here, because each length of res need time
- 2 conditions: 1. add the nums[i], 2.not add
- Time: O(n(2^n)), Space:O(n)

### [39. Combination Sum](https://github.com/liangliang1120/leetcode/blob/main/solutions/39-Combination-Sum.py)
- if sum(subset) == target: res.append(subset.copy())
- if i >= n or sum(subset) > target: return === i here represent as the index of num
- 1.subset add num[i] , bsf(i) === add it self, repeat num
- 2.pop, bsf(i+1) === add next num
- Time: up to O(n(2^n)), Space:O(target) - recursive stack

