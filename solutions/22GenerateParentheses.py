class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(l, r):
            if l == r and l == n:
                res.append(''.join(stack))
                return 
            if l > r:
                stack.append(')')
                backtrack(l, r + 1)
                stack.pop()
            if l < n:
                stack.append('(')
                backtrack(l + 1, r)
                stack.pop()
        backtrack(0, 0)
        return res
