# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # keep two pointers to keep track of the front and back of the list, find the kth element if it doesnt exist then we do nothing because not enough nodes in the group to reverse
        # if k nodes in the list to reverse keep a track of the previous of the list before reversing and the next of the list before reversing, reverse the list, make the pointers point to the correct ones and move on to the next
        # repeat this until we reach the end of the list or we cannot find a group of k nodes to reverse
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
