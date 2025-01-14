# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        the naive way to do this using O(n) time and O(n) space is to 
        put it in an array and then add it to the linked list and return it
        so lets do the naive approach first
        '''
        '''
        store = []
        store_current = head
        while store_current:
            store.append(store_current)
            store_current = store_current.next
        # now that we have them in an array lets rearrange them
        dummy = ListNode()
        current = dummy
        while store:
            current.next = store.pop(0)
            print(current.next.val)
            current = current.next
            current.next = None # this has to be done because the node put here has the old reference to the linked list and not the one we want
            if store:
                current.next = store.pop(-1)
                print(current.next.val)
                current = current.next
                current.next = None

        '''

        '''
        okay now we need to do this in place
        first we need to find the mid point of the list to reverse the second half
        second we need to reverse the second half
        then we need to merge both of them
        '''


        
        if not head:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        slow.next = None
        # now lets reverse the second half of the list
        prev = None
        while second_head:
            nxt = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = nxt

        # now the new head of the reversed list is prev
        rev_head = prev
        dummy = ListNode()
        curr = dummy
        while rev_head:
            curr.next = head
            head = head.next
            curr = curr.next
            curr.next = None
            curr.next = rev_head
            rev_head = rev_head.next
            curr = curr.next
            curr.next = None
        curr.next = head
            




               

        