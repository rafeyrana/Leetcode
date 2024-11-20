"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # since we have to clone the graph and only have one node and have to clone the neighbours as well this is a clear as day bfs implementation,
        # lets maintain a mapping of which node maps to which and then just clone all of them by appending their neighbours to the adjacency list of them while we are iterating


        if not node:
            return None
        node_map = {}

        def bfs(node):
            q = collections.deque()
            q.append(node)
            node_map[node] = Node(node.val)
            while q :
                current_node = q.popleft()
                for neigh in current_node.neighbors:
                    if neigh not in node_map:
                        node_map[neigh] = Node(neigh.val)
                        q.append(neigh)
                    node_map[current_node].neighbors.append(node_map[neigh])

        bfs(node)
        return node_map[node]









