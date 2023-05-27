class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        count = 1
        for l in range(1, len(s)):
            # print(l, res, count, s[l - 1], s[l])
            if s[l - 1] == s[l]:
                count += 1
            else:
                count = 1
            res = max(res, count)
        return res
