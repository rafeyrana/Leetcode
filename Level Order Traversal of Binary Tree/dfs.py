# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        '''
        keep track of the depth and the use that as the index to add the node val to the correct list
        '''
        results = []
        intial_depth = 0

        def dfs(node, depth):
            if not node:
                return None
            if len(results)== depth:
                results.append([])
            results[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, intial_depth)
        return results