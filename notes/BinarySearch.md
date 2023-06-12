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

### [704. Binary Search](https://github.com/liangliang1120/leetcode/blob/main/solutions/704-Binary-Search.py)


### [74. Search a 2D Matrix](https://github.com/liangliang1120/leetcode/blob/main/solutions/0074-Search-a-2D-Matrix.py)
- use n*m-1 to be the end, then use binary search
- Time: O(n*m), Space: O(1)



