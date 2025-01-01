# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # iterate through both lists until any of them exists
        # for each node check if the nodes are same or if any of the nodes are in the seen set
        # if in the seen set or they are the same return the node 
        # if not in it add to the visited set
        # return None as the value at the end of the function

        seen = set() # keep a set to keep a track of the nodes that we have visited
        while headA or headB:
            if headA == headB:
                return headA
            if headA in seen:
                return headA
            if headB in seen:
                return headB
            if headA:
                seen.add(headA)
                headA = headA.next
            if headB:
                seen.add(headB)
                headB = headB.next

        return None
