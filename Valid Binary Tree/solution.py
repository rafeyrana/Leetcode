# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        using a helper function we can set the upper and lower bound for each node to be valid. the upper values and lower values are set to float("-inf") and float("inf") intially for the root
        return false if the node is not a valid and in range. for the recursive call change the value for the right side to be bounded on the left by this nodes value and similarly for the left side to be bounded on the right by this nodes value
        the other side will be bounded by the previous left or right values.
        '''
        def validate(node, left_val, right_val):
            if not node:
                return True
            if not (left_val < node.val < right_val):
                return False
            return validate(node.left, left_val, node.val) and validate(node.right, node.val, right_val)
        

        return validate(root, float("-inf"), float("inf"))