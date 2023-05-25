### 3. [Longest Substring Without Repeating Characters](https://github.com/liangliang1120/leetcode/blob/main/solutions/twoPointers_3.py)
- visited = set()
- left指针在len中循环，while right指针<len(s) and s[j] not in visited: visied.add, right point 右移
- 过程中更新max_len,visited.remove(s[i])

### [125. Valid Palindrome](https://github.com/liangliang1120/leetcode/blob/main/solutions/125ValidPalindrome)
Time:O(n) space:O(1)
use ord to implement the function of alnum(alphanumeric)
2 pointers to check, while not alnum and l < r: move; if not ==, return false

## 253 meeting rooms2
开始时间和结束时间分成两个list并排序，各有一个指针
while startpoint 到len，每次循环，start指针+1，room+1；如果有开始时间 >= 结束时间的，end指针+1,room-1



