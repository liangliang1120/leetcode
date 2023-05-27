class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        res = 0
        sdict = defaultdict(int)
        while r < len(s):
            sdict[s[r]] += 1
            while sdict[s[r]] > 1:
                sdict[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
