# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        '''
        run dfs on this problem, get the left and right sum. now at this point we need to check if this node and its left and right are the max sum path. so first we do that
        and then we return the node.val + max(left, right) because the node above can only go to one of the sides below so we choose the max side
        
        '''
        self.max_sum = float("-inf")


        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            max_we_can_get_at_this_point = left + node.val + right
            self.max_sum = max(self.max_sum, max_we_can_get_at_this_point)
            return node.val + max(left, right)
        dfs(root)
        return self.max_sum
        