class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        j = 0
        max_len = 0
        
        for i in range(len(s)):
            while j < len(s) and s[j] not in visited:
                visited.add(s[j])
                j += 1
            max_len = max(max_len, j - i)
            visited.remove(s[i])
        return max_len
