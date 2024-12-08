class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # both the interval and the queries have to be sorted to go over them in a certain order
        # we will add only the queries that can be valid up to the current query and if their endings are not valid for this query we will remove them because they will not be useful even for the future queries as the queries are sorted anyways
        intervals.sort()
        min_heap = []
        results = {}
        interval = 0
        for q in sorted(queries):
            # add only the intervals which start before or at the given query so we dont have all the intervals in the heap only the ones that can be valid for this one
            while interval < len(intervals) and intervals[i][0] <= q:
                l , r = intervals[i]
                heapq.heappush(min_heap , (r - l + 1, r)) # save the interval length and the ending of it
                interval += 1 # keeping track of the current interval

            # remove and clean the heap by removing all the intervals which cannot contain q, since q is sorted this means they would not have been valid even for the future ones
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            # now if the heap still contains something in this interval then we can add it
            results[q] = min_heap[0][0] if min_heap else - 1
            return [results[q] for q in queries]


