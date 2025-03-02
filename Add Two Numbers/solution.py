# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # so since this number is arranged in reverse this helps us go from left to right in the number
        # if you use the primary school addition principle the number is added from units to tens to hundreds and so on
        # at each step we need to keep a track of the result of the addition of the two numbers on that unit and then store the carry to be carried over

        dummy = ListNode() # using the dummy node to store the head of the result list
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            result = l1_val + l2_val + carry
            result_new = result % 10 
            carry = result // 10 
            print(result_new)
            node = ListNode(result_new)
            current.next = node
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
        