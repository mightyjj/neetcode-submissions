"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        starts = sorted([s.start for s in intervals])
        ends = sorted([e.end for e in intervals])

        start_idx, end_idx = 0, 0
        curr_rooms, max_rooms = 0, 0
        while start_idx < len(starts):
            if starts[start_idx] < ends[end_idx]:
                curr_rooms += 1
                start_idx += 1
            else:
                curr_rooms -= 1
                end_idx += 1
            max_rooms = max(max_rooms, curr_rooms)
        
        return max_rooms