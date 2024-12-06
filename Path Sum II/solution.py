# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        '''
        this is going to be a dfs traversal with early stopping and an array to keep a track of the path uptil now as well as an array to keep a track of all the solutions
        the early stopping condition is if the sum is more than the target OR if equal to target and not a leaf node
        '''
        results = []

        def dfs(node, path, path_sum):
            if not node:
                return
            path_sum += node.val
            path.append(node.val)
            if path_sum == targetSum and not node.left and not node.right:
                results.append(list(path))  # Append a copy of the path
                path.pop()  
                return
            dfs(node.left, path, path_sum)
            dfs(node.right, path, path_sum)
            path.pop()  # Backtrack after both recursive calls

        dfs(root, [], 0)
        return results