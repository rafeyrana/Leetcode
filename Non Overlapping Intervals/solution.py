class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        we will use a greedy approach to this question
        intially we sort by starting time
        at each step we will check for an overlap with the previous intervals end
        if we find an overlap we will now have the chance to remove one of the intervals in this case. so to do this we will keep the end of the interval with the min end to reduce chance of it overlapping with any upcoming intervals
        if we dont find an overlap we change the prevEnd to the next ones en
        '''
        overlaps = 0
        intervals.sort()
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if prevEnd > start:
                overlaps += 1
                prevEnd = min(prevEnd, end) # keeping the interval with the min ending time to reduce the chance of overlap with the upcoming intervals
            else:
                prevEnd = end
        return overlaps
            
        