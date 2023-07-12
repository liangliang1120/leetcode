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


# java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> shash = new HashMap<>();
        Map<Character, Integer> thash = new HashMap<>();
        for (char c : s.toCharArray()) {
            shash.put(c, shash.getOrDefault(c, 0) + 1);
        }
        for (char c : t.toCharArray()) {
            thash.put(c, thash.getOrDefault(c, 0) + 1);
        }
        return thash.equals(shash);
    }
}
