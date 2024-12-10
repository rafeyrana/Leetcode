import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        this can be done by maintaining a max_heap of the most common characters and appending them together two at a time to avoid any issues of it being not adjacent
        while we have more than 2 elements in the heap we can keep alternating
        we breakout once we have only one left and check if it occurs more than once then we cant use it again and so need to return an empty string

        '''
        counts = Counter(s)
        
        # If the most frequent character appears more than (len(s) + 1) // 2, it's impossible
        if any(count > (len(s) + 1) // 2 for count in counts.values()):
            return ""
        heap = []
        for key, count in counts.items():
            heapq.heappush(heap, (-count, key))
        
        result = []
        
        while len(heap) > 1:
            count1, ch1 = heapq.heappop(heap)
            count2, ch2 = heapq.heappop(heap)
        
            result.append(ch1)
            result.append(ch2)
            
            # Push back the characters if there are remaining counts
            if count1 + 1 < 0:
                heapq.heappush(heap, (count1 + 1, ch1))
            if count2 + 1 < 0:
                heapq.heappush(heap, (count2 + 1, ch2))
        
        if heap:
            count, ch = heapq.heappop(heap)
            if -count > 1:
                return ""  # Cannot alternate anymore
            result.append(ch)
        
        return "".join(result)
