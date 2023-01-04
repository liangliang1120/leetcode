## 1-D Dynamic Programming

### 70. [Climbing Stairs](https://github.com/liangliang1120/leetcode/blob/main/dp_70.py)
- 从最后的结果开始，记录每个子问题的结果。
- 倒数第一个和倒数第二个的结果都是1, 每个位置的结果=前两步的子结果之和
- 1 1 2 3 5 ...
- one = 1, two = one, update one as one+two, two = previous one, finally return one
- time:O(n) space:O(1)

### 746. [Min Cost Climbing Stairs](https://github.com/liangliang1120/leetcode/blob/main/dp_746.py)
- 优化后只保存转移方程中两个元素：time:O(n) space:O(1)

### 198. [House Robber](https://github.com/liangliang1120/leetcode/blob/main/dp_198.py)
- 比较 rob1 + temp， rob2： 
- 状态转移方程： dp[i]表示打劫到第i个房子，最多能抢多少钱，dp[n]为所求：dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
- 最后返回rob2
- 优化后只保存转移方程中两个元素：time:O(n) space:O(1)

### 213. [House Robber II](https://github.com/liangliang1120/leetcode/blob/main/dp_213.py)
- 和上一题区别，房子在环上
- 拆解成两个问题： 0-n-1，1-n，再比较最大
- 状态转移方程： dp[i]表示打劫到第i个房子，最多能抢多少钱，dp[n]为所求：dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])


### 5. [Longest Palindromic Substring](https://github.com/liangliang1120/leetcode/blob/main/dp_5.py)
- brute force O(n*n^2)
- time: O(n^2) space:O(n^2)
- 从中间向两边，分res为奇数和偶数两种情况

### 647. [Palindromic Substrings](https://github.com/liangliang1120/leetcode/blob/main/dp_647.py)
- time: O(n^2) space:O(n^2)
- 与上一题思路相同，不用记录palindrome，直接记录数量

### 91. [Decode Ways](https://github.com/liangliang1120/leetcode/blob/main/dp_91.py)
- brute force: O(2^n)
- 类似于上楼梯的题目，上一个台阶还是上两个台阶，上台阶前判断是不是0，是不是小于等于26
- dp[i]表示前i个字符decode的种数，dp[n]为所求
- dp[0] = 1 空字符串的decode方式1种
- 方程：dp[i] = dp[i-1] + dp[i-2] 【1.i为一位数，而且i所在位置不能是0，种类即前面i-1位的种数】【2.i与前面一位组成两位数，i不能是前两个，组成的数字要<=26】
- 
- 
