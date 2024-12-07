class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        in this case we can implement a simple linear search to find the insertion point
        insertion point is where the ending point of the interval is less than the starting point of the interval

        '''
        n = len(intervals)
        i = 0
        results = []
        # adding the intervals that are before our insertion point
        while i < n and intervals[i][1] < newInterval[0]:
            results.append(intervals[i])
            i+=1


        # merging all the intervals that might be in our interval or need to be converted in our interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[1] = max(intervals[i][1],  newInterval[1])
            newInterval[0] = min(intervals[i][0],  newInterval[0])
            i += 1
        results.append(newInterval)

        # add the intervals remaining after it
        while i < n:
            results.append(intervals[i])
            i += 1

        return results

            
        

        