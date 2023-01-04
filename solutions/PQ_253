class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        free_rooms = []
        intervals.sort(key = lambda x: x[0])
        # 把最早的会议结束时间加进heap
        heapq.heappush(free_rooms, intervals[0][1])
        for i in intervals[1:]:
            # 如果当前会议开始时间 >= 前一个会议的结束时间
            if free_rooms[0] <= i[0]:
                # 把原来的pop
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms,i[1])
        return len(free_rooms)
