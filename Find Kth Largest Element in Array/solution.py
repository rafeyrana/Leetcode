import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        this is the same approach as the kth largest using heap
        since we need the kth largest we will use a min heap in this case and keep the size to k
        in the end we can return the heap[0]
        '''
        heap = []
        for num in nums:
                if len(heap) >= k:
                    heapq.heappushpop(heap, num)
                else:
                    heapq.heappush(heap, num)
        return heap[0]
        