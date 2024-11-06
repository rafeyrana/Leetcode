from collections import Counter
import heapq
class KthLargest:
    '''
    use a min heap to keep track of the k largest elements. so in this case when you pop it will be the kth largest element
    when adding add to the heap, readjust the heap to keep it at k elements. and then peek at the top of the heap to get the kth largest element
    '''
    def __init__(self, k: int, nums: List[int]):
        self.heap , self.k = nums, k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


        
