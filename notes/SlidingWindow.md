### [121. Best Time to Buy and Sell Stock](https://github.com/liangliang1120/leetcode/blob/main/solutions/121BestTimetoBuyandSellStock.py)
- fix the left pointer, only if profit < 0, update left; otherwise only move right pointer
- left and right start from 0 and 1
- while r < len, calculate profit, if profit < 0, left = right, update maxprofit, right ++
- Time: O(n), Space: O(1)

### [3. Longest Substring Without Repeating Characters](https://github.com/liangliang1120/leetcode/blob/main/solutions/3LongestSubstringWithout%20RepeatingCharacters.py)
- no matter use set or dict to make sure the substring without repeating
- left and right both start from 0
- right pointer move
- if has repeating character, left pointer move to right util no repeating character (the right pointer value) inside of the substring
- Time: O(n), Space: O(n)

### [424. Longest Repeating Character Replacement](https://github.com/liangliang1120/leetcode/blob/main/solutions/424LongestRepeatingCharacterReplacement.py)
- condition: windowsize - count(x) <= k
- if meet the condition: right pointer move a step to right
- if do not meet the condition: left pointer move a step to right
- update count(s[pointer]) first, then move the pointer
- windowsize can be counted each time pointer moves, or use (r - l + 1) then max(windowsize, r - l + 1)
- Time: O(n), Space: O(1)

### [567. Permutation in String](https://github.com/liangliang1120/leetcode/blob/main/solutions/567PermutationinString.py)
- use[0,0,...0] [num]*26 to present the slidingwidow's character number
- keep the slidingwindow size as s1, move the window to right, compare the [num]*26
- Time: O(n), Space: O(1)
