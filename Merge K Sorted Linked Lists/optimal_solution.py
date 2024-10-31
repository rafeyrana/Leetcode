# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # this can be done using a min heap as well
        # use the min heap to keep traversing the linked lists and adding nodes to them as long as they exist
        # the lists will be traversed on their own as the nodes get added to it
        # the min heap will keep track of the node with the smallest value regardless of which list it came from
    
        if not lists or len(lists) == 0:
            return None

        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy
        while min_heap:
            val, index, node = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next

            # Move to the next node in the list from which the node was taken
            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))

        return dummy.next