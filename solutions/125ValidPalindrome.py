class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isalnum(s[l]):
                l += 1
            while l < r and not self.isalnum(s[r]):
                r -= 1
            # print(s[l].lower(), s[r].lower(),l,r)
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


    def isalnum(self, c):
        if ord('A') <= ord(c) <= ord('Z') or \
            ord('a') <= ord(c) <= ord('z') or \
            ord('0') <= ord(c) <= ord('9'):
            return True
        return False
