class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        res = heapq.nlargest(k, nums, key=lambda x: x)
        return res[-1]
