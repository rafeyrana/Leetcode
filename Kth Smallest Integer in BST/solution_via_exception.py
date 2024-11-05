# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        in order traversal using a list and an exception to break the loop if the length of the list is equal to k and returning the last element of the list where it broke
        '''
        self.elements = []

        def in_order_traversal(node):
            if node:
                in_order_traversal(node.left)
                self.elements.append(node.val)
                if len(self.elements) == k:
                    raise done
                in_order_traversal(node.right)
        try:
            in_order_traversal(root)
        except:
            return self.elements[-1]

        