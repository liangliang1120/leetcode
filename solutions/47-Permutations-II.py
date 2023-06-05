class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = []
        res = []
        visited = [False] * n
        nums.sort()
        def backtrack():
            if len(subset) == n:
                res.append(subset.copy())
                return
            for i in range(n):
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                if not visited[i]:
                    visited[i] = True
                    subset.append(nums[i])
                    backtrack()
                    subset.pop()
                    visited[i] = False
           
        backtrack()
        return res
