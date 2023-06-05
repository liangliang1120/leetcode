class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
                if not visited[i]:
                    visited[i] = True
                    subset.append(nums[i])
                    backtrack()
                    subset.pop()
                    visited[i] = False

           
        backtrack()
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = []
        res = []
        def backtrack(i, visited):
            if i >= n:
                res.append(subset.copy())
                return
            for x in range(n):
                if not visited[x]:
                    subset.append(nums[x])
                    visited[x] = True
                    backtrack(i + 1, visited)
                    subset.pop()
                    visited[x] = False

        visited = [False for _ in range(n)]    
        backtrack(0,visited)
        return res
