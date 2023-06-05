class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        res = []
        n = len(candidates)
        candidates.sort()
        def backtrack(begin):
            if sum(subset) > target:
                return
            if sum(subset) == target:
                res.append(subset.copy())
                return
            for index in range(begin, n):
                if sum(subset) + candidates[index] > target:
                    break
                
                subset.append(candidates[index])
                backtrack(index)
                subset.pop()

        backtrack(0)
        return res

