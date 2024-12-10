import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        the intuition for this is go over the whole array, keep the value and their index, at each index that is out of the range of this sliding window we will keep popping them and then add the top of the heap to the results array
        '''
        results = []
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                results.append(-heap[0][0])
        return results