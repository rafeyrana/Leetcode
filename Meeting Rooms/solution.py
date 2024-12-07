"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        '''
        to be added to the schedule there should be no overlaps in the schedule of the meetings
        we will first sort by start times, write function to check overlaps, if there are overlaps then we will return false
        '''
        def checkOverlap(int1, int2):
            start = max(int1.start, int2.start)
            end = min(int1.end, int2.end)
            return end - start > 0


        if not intervals:
            return True
        intervals.sort(key=lambda x: int(x.start))
        prevInterval = intervals[0]
        for interval in intervals[1:]:
            if checkOverlap(prevInterval, interval):
                return False
            prevInterval = interval
        return True
                