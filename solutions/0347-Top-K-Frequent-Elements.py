class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hm = Counter(nums)
        hm = defaultdict(list)
        len_nums = len(nums)
        
        for n, c in count_hm.items():
            hm[c].append(n)
        # print(hm)
        res = []
        for i in range(len_nums, 0, -1):
            # if len(hm[i]) > 0:
            #     res.extend(hm[i])
            for n in hm[i]:
                res.append(n)
                if len(res) == k:
                        return res


# java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> occurrences = new HashMap<Integer, Integer>();
        for (int num : nums) {
            occurrences.put(num, occurrences.getOrDefault(num, 0) + 1);
        }

        // int[] 的第一个元素代表数组的值，第二个元素代表了该值出现的次数
        PriorityQueue<int[]> queue = new PriorityQueue<int[]>(new Comparator<int[]>() {
            public int compare(int[] m, int[] n) {
                return m[1] - n[1];
            }
        });
        for (Map.Entry<Integer, Integer> entry : occurrences.entrySet()) {
            int num = entry.getKey(), count = entry.getValue();
            if (queue.size() == k) {
                if (queue.peek()[1] < count) {
                    queue.poll();
                    queue.offer(new int[]{num, count});
                }
            } else {
                queue.offer(new int[]{num, count});
            }
        }
        int[] ret = new int[k];
        for (int i = 0; i < k; ++i) {
            ret[i] = queue.poll()[0];
        }
        return ret;
    }
}


class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map <Integer, Integer> countMap = new HashMap<>();
        for (int i : nums) {
            countMap.put(i, countMap.getOrDefault(i, 0) + 1);
        }
        Map <Integer, List<Integer>> frequencyMap = new HashMap<>();
        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            int num = entry.getKey();
            int count = entry.getValue();
            frequencyMap.put(count, frequencyMap.getOrDefault(count, new ArrayList<>()));
            frequencyMap.get(count).add(num);
            # frequencyMap.computeIfAbsent(count, key -> new ArrayList<>()).add(num);
        }

        int[] result = new int[k];
        int x = 0;
        for (int i = nums.length; i >= 0; i--) {
            if (x == k) {
                break;
            }
            if (frequencyMap.containsKey(i)) {
                for (int n : frequencyMap.get(i)) {
                    // System.out.println(n);
                    result[x] = n;
                    x++;
                }
            }
        }
        return result;
    }
}
