import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        okay so lets build an intuition for this first
        we need to keep a track of the heaviest stones to be at the top of the stack / heap 
        if equal dont push anything back
        if not equal push abs(x - y) back in the heap
        until size of heap is 1 which you return
        '''
        heap = [-stone for stone in stones] # make negative for max heap
        heapq.heapify(heap)
        # now we have the heap containing the stones in the heaviest position
        while len(heap) > 1:
            stone_x = -heapq.heappop(heap)
            stone_y = -heapq.heappop(heap)
            smash = abs(stone_x - stone_y)
            if smash != 0:
                heapq.heappush(heap, -smash)
        return -heap[0] if heap else 0

        