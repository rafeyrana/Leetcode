class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        in this case we cannot assume the intervals are sorted so first we will sort them by the start time
        once sorted we can break this problem down
         - check if they overlap
            - if they overlap check how to merge them
            - merging has full englufling or partial engulf
         - if they dont overlap just add the interval as is
        since we need to check each interval with the previous interval we need to make sure that we check with the ones that have already been checked and merged so we will make another array to keep a track of that as well
        '''

        def merge(int1, int2):
            start = min(int1[0], int2[0])
            end = max(int1[1], int2[1])
            return [start, end]


        def check_overlap(int1, int2):
            start = max(int1[0], int2[0])
            end = min(int1[1], int2[1])
            return end - start >= 0

        intervals.sort() # sorting by starting index
        results = []
        results.append(intervals[0])

        for interval in intervals[1:]:
            prev_interval = results[-1]
            # now lets check if they are overlapping or not
            if check_overlap(prev_interval, interval):
                # if they overlap we will merge
                new_interval = merge(prev_interval , interval)
                results.pop() # remove the old interval from the list as it has not been merged
                results.append(new_interval)

            else:
                results.append(interval)

        return results


