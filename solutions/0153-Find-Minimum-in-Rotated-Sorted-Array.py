class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[n-1] > nums[0]:
            return nums[0]
        start, end = 0, n - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
        return min(nums[start], nums[end])
