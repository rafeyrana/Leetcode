# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        if not root return 0, if the root and does not have right and left children return 1, after these, just make depth and add one and add the max of the recursive function for both sides
        ''' 


        if not root :
            return 0
        if not root and not root.left and not root.right:
            return 1
        depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return depth
        