"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        to visualise this is a better idea, so what we need to find out is what the maximum number of meetings going on at each time which will be the the number of days we need
        now this means that on a number line we need to find out simultaneously which meetings are going on and which are done
        lets start by sorting an array of the start and end times, we will keep a pointer for which time is being processed right now,
        at each time we will get the min of the values of the two pointers and then process them
        the counter which we need to keep a track of will be incremented when we find a lesser start time and will be decremented when we find a less end time. in case of them begin the same we wil favour the end time because they are considered non overlapping if on the same one
        '''
        if not intervals :
            return 0
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        s = e = counter = 0
        max_count = -1

        while s < len(intervals):
            if start[s] < end[e]:
                counter += 1
                s += 1
            else:
                counter -= 1
                e += 1
            max_count = max(max_count, counter)
        return max_count


        