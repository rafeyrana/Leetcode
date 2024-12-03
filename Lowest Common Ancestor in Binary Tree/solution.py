# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        since this is a binary tree we know the nodes will be in ascending sorted order and we can restrict our search space using this
        if either val is equal to the root val then that is the LCA
        if either of p or q is bigger than the root and the other is smaller, the root will become the lowest common ancestor
        if both are smaller then reduce search space to search on left sub tree
        if both are bigger then reduce search space to search on right sub tree
        '''
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            LCA = root
            return LCA
        elif (root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val):
            LCA = root
            return LCA
        elif (root.val < p.val and root.val <q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif (root.val > p.val and root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)