### 20. [Valid Parentheses](https://github.com/liangliang1120/leetcode/blob/main/solutions/Stack_20.py)
input只有括号，if len不被2整除 false。pair = {")": "(", "]":"[", "}":"{"} 
循环每个character,如果ch in pair,if not stack or stack[-1] != pair[ch]:false（没有前半个括号 或者 最近的括号不匹配
pop;如果ch not in pair,stack.append.  return not stack


### 1628. [Design an Expression Tree With Evaluate Function](https://github.com/liangliang1120/leetcode/blob/main/solutions/Stack_1628.py)


### 227. [Basic Calculator II](https://github.com/liangliang1120/leetcode/blob/main/solutions/Stack_227.py)
- stack从0开始，除法注意负数情况（-1），乘法要先pop再*
- 更新preSign
