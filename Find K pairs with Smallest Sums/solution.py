from heapq import heappush , heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        okay since we know that we have to keep a track of the minimum pairs and since we know this a sorted list we will try to find them from the first index of both, add that to our heap and add at the end append it to the results list, then we will move the pointer for both arrays along one by one to see which combo is more valid by adding them to the heap and popping from the next time until we have a total of k elements popped
        we will also keep a track of the visited index combos
        '''
        if not k or not nums1 or not nums2:
            return []
        results = []
        heap = []
        heappush(heap, (nums1[0]+ nums2[0], 0, 0))
        visited = set()
        visited.add((0,0))
        while k and heap:
            res, i, j = heappop(heap)
            results.append((nums1[i], nums2[j]))
            if (i + 1) < len(nums1) and (i + 1, j) not in visited:
                heappush(heap, (nums1[i + 1]+ nums2[j], i + 1, j))
                visited.add((i + 1, j))
            
            if (j + 1) < len(nums2) and (i, j + 1) not in visited:
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
            
            k -= 1
        return results
            

            

