### [121. Best Time to Buy and Sell Stock](https://github.com/liangliang1120/leetcode/blob/main/solutions/121BestTimetoBuyandSellStock.py)
- fix the left pointer, only if profit < 0, update left; otherwise only move right pointer
- left and right start from 0 and 1
- while r < len, calculate profit, if profit < 0, left = right, update maxprofit, right ++
- Time: O(n), Space: O(1)