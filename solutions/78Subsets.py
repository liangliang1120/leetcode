class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        subset = []
        def backtrack(i):
            if i >= n:
                res.append(subset.copy())
                return
            # include the nums[i]
            subset.append(nums[i])
            backtrack(i + 1)
            # not include nums[i]
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res

