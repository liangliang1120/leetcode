class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = []
        res = []
        nums.sort()
        def backtrack(start):
            res.append(subset.copy())
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        backtrack(0)
        return res
    
    
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
