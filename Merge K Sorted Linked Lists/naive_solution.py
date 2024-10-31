# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        make a new list which will be the merged list
        for the list of heads of the linked list for each pass, keep a track of the min value at the node
        pointed to by the head in the list and once a pass over the array is done, make that node go to next
        if any node is pointing to null then skip it
        when the min value does not change or the index is not updated for any pass over the list means that all lists have been exhausted and there are no more.
        '''
        if not lists:
            return None
        if not lists[0]:
            return None

        dummy = ListNode(0)
        current = dummy
        while True:
            min_node_on_each_pass = [float("inf"),-1] # list containing the value and index at which the minimum occurs, that is the one that we have to change
            for index, node in enumerate(lists):
                if node:
                    if node.val <= min_node_on_each_pass[0]:
                        min_node_on_each_pass[0] = node.val
                        min_node_on_each_pass[1] = index
            if min_node_on_each_pass[1] == -1: # meaning in this pass there was no minimum and all were none meaning the lists are finished
                break
            lists[min_node_on_each_pass[1]] = lists[min_node_on_each_pass[1]].next
            current.next = ListNode(min_node_on_each_pass[0])
            current = current.next

        return dummy.next

        
        