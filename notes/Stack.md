### [20. Valid Parentheses](https://github.com/liangliang1120/leetcode/blob/main/solutions/20ValidParentheses.py)
- if stack and stack[-1] == hashmap[s[i]]: stack.pop() else: return False
- input只有括号，if len不被2整除 false。pair = {")": "(", "]":"[", "}":"{"} 
- 循环每个character,如果ch in pair,if not stack or stack[-1] != pair[ch]:false（没有前半个括号 或者 最近的括号不匹配
- pop;如果ch not in pair,stack.append.  return not stack
- Time: O(n), Space: O(n)

### [155. Min Stack](https://github.com/liangliang1120/leetcode/blob/main/solutions/155MinStack.py)
- use another min_stack to track the min number, only record the minimum
- 2 tips
- - if not self.min_stack or x <= self.min_stack[-1]: min_stack.append(x) | (<=) to record each min number,if 2 min number
- - x = stack.pop();  if min_stack[-1] == x: | use the x value here(need to pop the num no matter it's min or in the middle of min_stack)
- Time: O(1), Space: O(n)

### [150. Evaluate Reverse Polish Notation](https://github.com/liangliang1120/leetcode/blob/main/solutions/150EvaluateReversePolishNotation.py)
- 2 tips
- - truncates toward zero: int(x/y)
- - return int(stack[-1]) (int datastructure type)
- Time: O(n), Space: O(n)

### [22. Generate Parentheses](https://github.com/liangliang1120/leetcode/blob/main/solutions/22GenerateParentheses.py)
- all combinations: backtrack
- use a stack as the temp
- 3 conditions in backtrack: （Parallel， each time in a backtrack should check 3 conditions)
- - 1. left = right = n: add the stack to res
- - 2. close parentheses < open parentheses: add close parentheses
- - 3. open parentheses < n: can add open parentheses
- Time: O((4^n)/(n^0.5)), Space: O(n) [Time:.., Space: for stack]

### 1628. [Design an Expression Tree With Evaluate Function](https://github.com/liangliang1120/leetcode/blob/main/solutions/Stack_1628.py)


### 227. [Basic Calculator II](https://github.com/liangliang1120/leetcode/blob/main/solutions/Stack_227.py)
- stack从0开始，除法注意负数情况（-1），乘法要先pop再*
- 更新preSign
