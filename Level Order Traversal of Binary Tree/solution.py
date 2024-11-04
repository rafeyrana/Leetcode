# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        using bfs, enque the first node and then dequeue it and add its children to the queue. the trick here is the inner loop which only runs for the length of the queue after each levels children have been added so will only iterate for the level
        '''

        # using bfs
        q = collections.deque()
        q.append(root)
        results = []
        while q:
            level = []
            level_len = len(q) # will only contain the nodes at some level after going through all the nodes in a levl
            for i in range(level_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                results.append(level)
        return results