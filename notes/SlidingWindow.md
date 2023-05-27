### [121. Best Time to Buy and Sell Stock](https://github.com/liangliang1120/leetcode/blob/main/solutions/121BestTimetoBuyandSellStock.py)
- fix the left pointer, only if profit < 0, update left; otherwise only move right pointer
- left and right start from 0 and 1
- while r < len, calculate profit, if profit < 0, left = right, update maxprofit, right ++
- Time: O(n), Space: O(1)

### [3. Longest Substring Without Repeating Characters](https://github.com/liangliang1120/leetcode/blob/main/solutions/3LongestSubstringWithout%20RepeatingCharacters.py)
- no matter use set or dict to make sure the substring without repeating
- left and right both start from 0
- right move, and check whether include repeating character
- if has repeating character, left pointer move to right util no repeating character inside of the substring
- Time: O(n), Space: O(n)
