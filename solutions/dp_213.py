class Solution:
    def _rob(self, nums: List[int]) -> int:
        dp0 = dp1 = 0
        for i in range(len(nums)):
            dp0, dp1 = dp1, max(dp0 + nums[i], dp1)
        return dp1
    
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(self._rob(nums[:-1]), self._rob(nums[1:]))
    
