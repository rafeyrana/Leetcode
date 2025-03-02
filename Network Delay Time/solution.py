import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        n directed nodes - 1 indexed
        u -> v where u is any source node and v is any destination node and t is the time here
        k is the real source node


        make an array of each node being touched, if the list is not n long then just remove it

        finding the shortest path here
        
        '''
        # first lets make the adjacency list
        adj_list = defaultdict(list)
        for u, v, t in times:
            adj_list[u].append((t, v))  # (time, destination)

        # for each node we will add their neighbours to our min heap and we will visit that node
        min_heap = [(0, k)]  # (time, node)
        heapq.heapify(min_heap)

        visit = set()
        min_time = 0

        while min_heap:
            t, node = heapq.heappop(min_heap)
            if node in visit:
                continue
            visit.add(node)
            min_time = t

            for ti, dest in adj_list[node]:
                if dest not in visit:
                    heapq.heappush(min_heap, (t + ti, dest))  
        
        return min_time if len(visit) == n else -1  # Return -1 if not all nodes are visited