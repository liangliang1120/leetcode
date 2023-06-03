class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n = len(nums)
        nums.sort()
        def backtrack(i):
            if i >= n:
                res.append(subset.copy())
                return
            # 1 
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            #2
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        
        backtrack(0)
        return res
