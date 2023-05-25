## 217. [Contains Duplicate](https://github.com/liangliang1120/leetcode/blob/main/solutions/Hashing_217.py)
brute force:O(n^2), O(1)
sort: O(nlogn) O(1)
hash:O(n) O(n)

## [242. Valid Anagram](https://github.com/liangliang1120/leetcode/blob/main/solutions/HashTable_242.py)
hash:O(n) O(n)

## 128. Longest Consecutive Sequence
set,if i-1 in set:continue else:while i+1 in set:curr_len+1,max(curr_len,max_len),return max_len

## [1. Two Sum](https://github.com/liangliang1120/leetcode/blob/main/solutions/hashing_1)
存hashtable for i,n in enumerate(nums): if target - n in hashtable:return [hash[target - n],i]
{n:i}
time O(n) space O(n)

## 3 sum
i 循环 右边部分开头左指针， 结束右指针，
1）三数之和=0，append，
left < right and 左指针一直和后面的相等，左指针++，
left < right and 右指针一直和前面的相等，右指针--，
再分别fen bie++，--，
2）三数之和>0 right--;
3）三数之和>0 left++;
time O(N^2) space(N)

## 49 [Group Anagrams](https://github.com/liangliang1120/leetcode/blob/main/solutions/Sort_49.py)
defaultdict（list)  "".join(sorted(list(s))) mp[key].append(s),time O(nklogk) space O(nk) 字符串数量，k字符串最大长度
brute force Time:O(m*nlogn)
26 characters:
time: O(mn26),M is the number of words,n is the average length of a word,

## 347 [Top K Frequent Elements](https://github.com/liangliang1120/leetcode/blob/main/solutions/347Top_K_Frequent_Elements.py)
key is the frequency, value is the numbers
Time: O(n), Space: O(n)


## [238. Product of Array Except Self](https://github.com/liangliang1120/leetcode/blob/main/solutions/238ProductofArrayExceptSelf.py)
compute the prefix and postfix and then get the outcome
Time: O(n), Space: O(n)

## 133clone graph
如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回;
克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表 // 哈希表存储 // 遍历该节点的邻居并更新克隆节点的邻居列表

## 138. 复制带随机指针的链表
先存每个node 每个node对应的顺序，然后再循环，建立连接
for i in range(len(copy)):
            if i < len(copy) - 1:
                copy[i][0].next = copy[i+1][0]
            if copy[i][1]:
                copy[i][0].random = copy[node2index[copy[i][1]]][0]
                
### [1282. Group the People Given the Group Size They Belong To](https://github.com/liangliang1120/leetcode/blob/main/solutions/hashTable_1282)
- ans = [], mp = dict()
- 一次循环，如果value为空，ans.append([i]) mp[v] = len(ans) 
- 用mp记住当前ans第几个已经满了，接着加进ans

### 387. [First Unique Character in a String](https://github.com/liangliang1120/leetcode/blob/main/solutions/hashTable_387.py)

### 146. [LRU Cache](https://github.com/liangliang1120/leetcode/blob/main/solutions/hashTable_146.py)


