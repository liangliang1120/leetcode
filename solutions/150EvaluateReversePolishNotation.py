class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for c in tokens:
            if c not in ['+', '-', '*', '/']:
                stack.append(c)
            else:
                x = stack.pop()
                y = stack.pop()
                if c == '+':
                    stack.append(int(y) + int(x)) 
                if c == '-':
                    stack.append(int(y) - int(x)) 
                if c == '*':
                    stack.append(int(y) * int(x)) 
                if c == '/':
                    stack.append(int(int(y) / int(x))) 
            # print(stack)
        return int(stack[-1])
