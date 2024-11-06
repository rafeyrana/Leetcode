import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        similar to k largest but here we can keep a max heap to maintain the k closest elements in the heap and pop out the others when the length of the heap is greater than k.
        '''
        heap = [] # this will be our max heap
        for idx, coor in enumerate(points):
            distance = - ((coor[0])**2 + (coor[1])**2)
            if len(heap) >= k:
                heapq.heappushpop(heap, (distance, idx))
            else:
                heapq.heappush(heap,(distance, idx))
        return [points[idx] for _, idx in heap]
         



        