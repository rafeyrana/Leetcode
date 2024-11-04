# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        the concept of the question is to get the right side view of the tree, does not necessarily have to be the right children all the way down, implement bfs and get the last child at each level to get the right side view
        '''

        q = collections.deque()
        result = []
        q.append(root)
        while q:
            level_length = len(q)
            for i in range(level_length):
                node = q.popleft()
                if node:
                    if i == level_length - 1: # last node in the level
                        result.append(node.val)
                    # Append children to the queue if they exist
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return result
