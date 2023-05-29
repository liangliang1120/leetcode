class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1count = [0] * 26
        s2count = [0] * 26
        for c in s1:
            s1count[ord(c) - ord("a")] += 1
        l, r = 0, len(s1) - 1
        for i in range(l, r + 1):
            s2count[ord(s2[i]) - ord("a")] += 1
        while r < len(s2) - 1:
            if s2count == s1count:
                return True
            s2count[ord(s2[l]) - ord("a")] -= 1
            r += 1
            l += 1
            s2count[ord(s2[r]) - ord("a")] += 1
        if s2count == s1count:
                return True
        return False
