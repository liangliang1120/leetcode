class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if index > begin and candidates[index] == candidates[index - 1]:
                    continue
                
                subset.append(candidates[index])
                backtrack(index + 1)
                subset.pop()

        backtrack(0)
        return res
