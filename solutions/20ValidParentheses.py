class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'}': '{', ')': '(', ']': '['}
        for i in range(len(s)):
            if s[i] in hashmap:
                if stack and stack[-1] == hashmap[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if len(stack) == 0:
            return True
        return False
