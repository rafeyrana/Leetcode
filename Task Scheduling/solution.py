class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        we will need to use a heap to keep a track of the most occuring tasks at each time frame to try to execute them first as they are the major blockers
        once a task has been executed the next occurence of the task can only be after the cooldown period has ended

        to keep a track of the most occcuring task at each time frame we will use a heap, we will only store the number of occurences as the name of the task does not matter in the final minimum cpu cycle executions needed
        when we execute the cpu command we will add it to a queue with the time at which the cooldown will be over, once it is over we can add it back to the heap
        the heap will contain the number of occurences and the queue will contain the number of tasks occurences remaining as well as the cooldown period end
        '''
        counts = collections.Counter(tasks)
        heap = [-cnt for item , cnt in counts.items()]
        heapq.heapify(heap)
        q = deque() # queue to keep a track of the cooldown time (-cnt, expiry time)
        time = 0
        while heap or q:
            time += 1
            
            if heap: # if there is a task to be executed at this time
                #execute it
                val = heapq.heappop(heap) + 1
                if val:
                    # add it the coolddown queue
                    q.append([val, time + n])
            else:
                time = q[0][1] # skip ahead in time to find the time of the first task to execute
            if q and q[0][1] == time: # meaning that the task at the first of the queue has finished its cooldown period
                heapq.heappush(heap, q.popleft()[0])
        return time

                


        