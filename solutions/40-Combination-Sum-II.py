class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        subset = []
        candidates.sort()
        def backtrack(i):
            if sum(subset) == target and subset not in res:
                res.append(subset.copy())
            if i >= n or sum(subset) > target:
                return
            # 1
            subset.append(candidates[i])
            backtrack(i + 1)
            subset.pop()
            # 2
            while i < n - 1 and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i + 1)
        backtrack(0)
        return res
