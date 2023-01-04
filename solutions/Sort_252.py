class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        for i in range(1, len(intervals)):
            meeting = intervals[i]
            last_meeting = intervals[i-1]
            if meeting[0] < last_meeting[1]:
                return False
        return True
