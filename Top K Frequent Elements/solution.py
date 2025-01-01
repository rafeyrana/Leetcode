class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the count of every single element, add to heap, pop the minimum values if it exceeds k then we pop from it. in the end we add the reverse of the list and the values of it
        counts = collections.Counter(nums)
        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (counts[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        results = []
        for i in range(len(heap) - 1, -1, -1):
            results.append(heap[i][1])
        return results



        