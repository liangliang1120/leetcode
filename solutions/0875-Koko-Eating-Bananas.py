class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(piles, speed, h):
            hrs = 0
            for pile in piles:
                hrs += ((pile - 1) // speed + 1)
            return True if hrs <= h else False

        start, end = 1, max(piles)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if can_finish(piles,mid,h):
                end = mid
            else:
                start = mid
        if can_finish(piles,start,h):
            return start
        if can_finish(piles,end,h):
            return end

        
