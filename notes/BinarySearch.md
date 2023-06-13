```
模板(背诵)：
start, end = ..,..
while start + 1 < end:
	mid = start + (end - start) // 2
	if some_condition(mid) == target:
		return mid
	elif some_condition(mid) < target:
		start = mid
	else:
		end = mid
if some_condition(start) == target:
	return start
if some_condition(end) == target:
	return end
return -1
```

## 1. find the condition: max result, min result


### [704. Binary Search](https://github.com/liangliang1120/leetcode/blob/main/solutions/704-Binary-Search.py)


### [74. Search a 2D Matrix](https://github.com/liangliang1120/leetcode/blob/main/solutions/0074-Search-a-2D-Matrix.py)
- use n*m-1 to be the end, then use binary search
- Time: O(n*m), Space: O(1)

### [875. Koko Eating Bananas](https://github.com/liangliang1120/leetcode/blob/main/solutions/0875-Koko-Eating-Bananas.py)
- the some_condition(mid) is that can finish eating, def a function can_finish(self, piles, speed, h): if need_hour <= h, true
- hrs += ((pile - 1) // speed + 1), --> math.ceil()
- start, end = 1, max(piles)
- mid = start + (end - start) // 2; if can_finish(piles,mid,h): end = mid 
- Time: O(nlogm), n = len(piles),m = max(piles), binary search: logm
- Space: O(1)


### [153. Find Minimum in Rotated Sorted Array](https://github.com/liangliang1120/leetcode/blob/main/solutions/0153-Find-Minimum-in-Rotated-Sorted-Array.py)
- if already sorted: return nums[0]
- binary search
- return min(start,end)
- Time: O(logn), Space: O(1)

### [33. Search in Rotated Sorted Array](https://github.com/liangliang1120/leetcode/blob/main/solutions/0033-Search-in-Rotated-Sorted-Array.py)
- when should move the start pointer to mid? 3 conditions: s<=m<t, t<m<=s, m<t<s
- Time: O(logn), Space: O(1)

### [981. Time Based Key-Value Store](https://github.com/liangliang1120/leetcode/blob/main/solutions/0981-Time-Based-Key-Value-Store.py)
- binary search find the time < target_time
- Time: O(logn), Space: O(n)


