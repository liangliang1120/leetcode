class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        wcount = defaultdict(int)
        max_count = 0
        ws = 0 # windowsize
        for r in range(len(s)):
            ws += 1
            wcount[s[r]] += 1
            max_count = max(max_count, wcount[s[r]])
            if ws - max_count <= k: # meet the condition
                pass
            else: # do not meet the condition
                wcount[s[l]] -= 1
                l += 1
                ws -= 1
        return ws

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        wcount = defaultdict(int)
        max_count = 0
        res = 0
        for r in range(len(s)):
            wcount[s[r]] += 1
            max_count = max(max_count, wcount[s[r]])
            if r - l + 1 - max_count <= k: # meet the condition
                pass
            else: # do not meet the condition
                wcount[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
