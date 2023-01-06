## 1-D Dynamic Programming

### 70. [Climbing Stairs](https://github.com/liangliang1120/leetcode/blob/main/solutions/dp_70.py)
- 从最后的结果开始，记录每个子问题的结果。
- 倒数第一个和倒数第二个的结果都是1, 每个位置的结果=前两步的子结果之和
- 1 1 2 3 5 ...
- one = 1, two = one, update one as one+two, two = previous one, finally return one
- time:O(n) space:O(1)

### 746. [Min Cost Climbing Stairs](https://github.com/liangliang1120/leetcode/blob/main/solutions/dp_746.py)
- 优化后只保存转移方程中两个元素：time:O(n) space:O(1)

### 198. [House Robber](https://github.com/liangliang1120/leetcode/blob/main/solutions/dp_198.py)
- 比较 rob1 + temp， rob2： 
- 状态转移方程： dp[i]表示打劫到第i个房子，最多能抢多少钱，dp[n]为所求：dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
- 最后返回rob2
- 优化后只保存转移方程中两个元素：time:O(n) space:O(1)

### 213. [House Robber II](https://github.com/liangliang1120/leetcode/blob/main/solutions/dp_213.py)
- 和上一题区别，房子在环上
- 拆解成两个问题： 0-n-1，1-n，再比较最大
- 状态转移方程： dp[i]表示打劫到第i个房子，最多能抢多少钱，dp[n]为所求：dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])


### 5. [Longest Palindromic Substring](https://github.com/liangliang1120/leetcode/blob/main/solutions/dp_5.py)
- brute force O(n*n^2)
- time: O(n^2) space:O(n^2)
- 从中间向两边，分res为奇数和偶数两种情况

### 647. [Palindromic Substrings](https://github.com/liangliang1120/leetcode/blob/main/solutions/dp_647.py)
- time: O(n^2) space:O(n^2)
- 与上一题思路相同，不用记录palindrome，直接记录数量

### 91. [Decode Ways](https://github.com/liangliang1120/leetcode/blob/main/solutions/dp_91.py)
- brute force: O(2^n)
- time: O(n) space:O(n)
- 类似于上楼梯的题目，上一个台阶还是上两个台阶，上台阶前判断是不是0，是不是小于等于26
- 对于s某个位置i，只关心i位置是否可以形成独立的一个解码，与前面的i-1位置能否形成一种解码

- dp[i]表示前i个字符decode的种数，dp[n]为所求
- 对于s某个位置i,有三种情况
- 转移方程：
- dp[i] = dp[i-1], 1<= a <=9 只能由i单独解码
- dp[i] = dp[i-2], 10<= b <=26 只能与前一位共同解码
- dp[i] = dp[i-1] + dp[i-2], 1<= a <=9, 10<= b <=26

### 322. [Decode Ways](https://github.com/liangliang1120/leetcode/blob/main/solutions/dp_322.py)
- time: O(n*amount) space:O(amount)
- dp[i]表示合成i需要的硬币数量，dp[amount]为所求
- 转移方程：
- dp[i] = min(dp[i], dp[i-coin] + 1)


### 152. [Maximum Product Subarray](https://github.com/liangliang1120/leetcode/blob/main/solutions/dp_152.py)
- subarray要是连续的 
- brute force O(n^2)
- 分情况，根据正负性讨论 keep tracking both positive and negative, keep the max and the min
- 使用前一位的max and min keep current the max and the min
- edge case: 0; reset our max and min to 1
- curMax = max(n * curMax, n * curMin, n)
- curMin = min(tmp, n * curMin, n)
- O(n) O(1)





