### 912. [Sort an Array](https://github.com/liangliang1120/leetcode/blob/main/solutions/Sort_912.py)
- quick sort

### 1636. [Sort Array by Increasing Frequency](https://github.com/liangliang1120/leetcode/blob/main/solutions/Sort_1636)
- Counter计数
- nums.sort(key=lambda x: (cnt[x], -x)) cnt先排升序，x降序


### 49. [Group Anagrams](https://github.com/liangliang1120/leetcode/blob/main/solutions/Sort_49.py)
- 排序后加进dict
- return list(dict.values)

### 252. [Meeting Rooms](https://github.com/liangliang1120/leetcode/blob/main/solutions/Sort_49.py)
- 开始时间排序
- 从第二个开始循环，有开始时间<下一个结束时间：false
