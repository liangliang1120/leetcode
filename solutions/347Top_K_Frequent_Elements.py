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
