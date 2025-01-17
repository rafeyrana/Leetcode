# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # this is a simple level order traversal approach where we can add to the list of nodes and then keep adding to for each level in the iteration of the list
        def bfs(node):
            if not node:
                return []
            q = collections.deque()
            q.append(node)
            levels = []
            while q:
                level = []
                for _ in range(len(q)):
                    n = q.popleft()
                    level.append(n.val)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                levels.append(level)
            return levels
        return bfs(root)
                    
                