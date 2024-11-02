# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        if both are null return true
        if one is null return false
        if values are not equal return false
        recursively check if left and right subtrees are same by calling the same function on their left and right nodes.
        '''
        if not p and not q:
            return True
        if not p or not q:
            return False
        if not p.val == q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        