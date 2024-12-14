class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        '''
        define a function for checking overlap and return the bool and the value of the overlap, if there exists an overlap add it to the list
        we will run a two pointer approach on the lists, we will only increment the counter of the list with the lower ending position of the two current intervals which will allow us to check for future intersections as the sets are disjoint meaning that if the smaller one is gone there is no scenario in which it is coming again
        
        '''
        
        def checkOverlap(i1, i2):
            start = max(i1[0], i2[0])
            end = min(i1[1], i2[1])
            overlap = end - start
            return overlap >= 0 , [start, end]

        if not firstList or not secondList:
            return []
        c1 = 0
        c2 = 0
        results = []
        while c1 < len(firstList) and c2 < len(secondList):
            interval1 = firstList[c1]
            interval2 = secondList[c2]
            overlap , overlap_interval = checkOverlap(interval1, interval2)
            if overlap:
                results.append(overlap_interval)
            if interval1[1] < interval2[1]:
                c1 += 1
            else:
                c2 += 1
        return results
            
            

            

            