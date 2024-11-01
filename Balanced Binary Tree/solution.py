# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        okay so the naive approach in this case would be be to call the depth function on each and every node and compare the difference and move to the next nodes below O(n**2)
        but the most efficient way to do this is bottoms up
        so start at the bottom most node, check if it is balanced, and return its height
        at the parent node check the condition for left and right being balanced and the height condition and pass that back with the updated height
        '''
        def dfs(curr): # returns at tuple of (balanced, height)
            if not curr:
                return [True, 0]
            left , right = dfs(curr.left), dfs(curr.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <=1

            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]



        