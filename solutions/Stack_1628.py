'''
O(N) iterate
O(N) stack
加号：将数字压入栈；
减号：将数字的相反数压入栈；
乘除号：计算数字与栈顶元素，并将栈顶元素替换为计算结果。
'''

class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        preSign = '+'
        num = 0
        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0') # 按位去读，所以要*10，例如42
            if i == n - 1 or s[i] in '+-*/':
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num) #pop 再*
                else:
                    stack.append(int(stack.pop() / num)) # 除法， -3/2=-1， -3//2=-1.5=-2 要加1
                preSign = s[i]
                num = 0
        return sum(stack)

# print(-3/2) -1.5
# print(-3//2) -2
# print(int(-3//2)) -2
# print(int(-3/2)) -1
