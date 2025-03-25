import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first we will need the frequency of all the elements in the array
        counts = collections.Counter(nums)
        # now the most simple way to do this is to sort it by count and get the [len(nums) -k + 1:] elements or [:k] if we sort in reverse
        # this will result in O(NlogN) complexity because that is the best we can do with sorting
        # another approach is to maintain a max heap of size k and when the size of the heap is more than k we pop from the array and in the end we return the heap
        # insertion in the heap is O(logN) because it is a self balancing binary tree underneath and heapify is o(n) so we will do this one by one
        print(counts)
        heap = []
        # heap = heapq.heapify(heap)
        for val, count in counts.items():
            if not heap or len(heap) < k:
                heapq.heappush(heap, (count, val))
                print("here")
            else:
                heapq.heappushpop(heap, (count, val))
        return [val for cnt, val in heap]
            