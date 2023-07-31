class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if nums == []:
        #     return 0
        hash_set = set(nums)
        sequence = defaultdict(list)
        for n in hash_set:
            if n - 1 not in hash_set:
                sequence[n].append(n)
                start = n
                while start + 1 in hash_set:
                    sequence[n].append(start + 1)
                    start += 1
        res = 0   
        for k in sequence.keys():
            if len(sequence[k]) > res:
                res = len(sequence[k])
        return res


# java
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        Set<Integer> hashSet = new HashSet<>();
        for (int num : nums) {
            hashSet.add(num);
        }

        Map<Integer, List<Integer>> sequence = new HashMap<>();
        for (int n : hashSet) {
            if (!hashSet.contains(n - 1)) {
                List<Integer> list = new ArrayList<>();
                list.add(n);
                int start = n;
                while (hashSet.contains(start + 1)) {
                    list.add(start + 1);
                    start++;
                }
                sequence.put(n, list);
            }
        }

        int res = 0;
        for (List<Integer> list : sequence.values()) {
            res = Math.max(res, list.size());
        }

        return res;
    }
}
