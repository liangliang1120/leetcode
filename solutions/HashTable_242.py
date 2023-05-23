class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        shash = defaultdict(int)
        thash = defaultdict(int)

        for sn in s:
            shash[sn] += 1
        for tn in t:
            thash[tn] += 1
        return thash == shash
