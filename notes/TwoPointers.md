### 3. [Longest Substring Without Repeating Characters](https://github.com/liangliang1120/leetcode/blob/main/solutions/twoPointers_3.py)
- visited = set()
- left指针在len中循环，while right指针<len(s) and s[j] not in visited: visied.add, right point 右移
- 过程中更新max_len,visited.remove(s[i])



## 253 meeting rooms2
开始时间和结束时间分成两个list并排序，各有一个指针
while startpoint 到len，每次循环，start指针+1，room+1；如果有开始时间 >= 结束时间的，end指针+1,room-1



