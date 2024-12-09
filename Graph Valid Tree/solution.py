class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        a tree is basically a directed acyclic graph, which means that even if it is undirected in this case it still cannot contain a cycle.
        we have the edges from which we can build the adjacency list, once we start travelling from the nodes and then to their neighbours we will keep a track of the visited nodes, if a node is visited again we have a cycle and it is not a tree
        since the edges are undirected the current node will also exist in its neighbours adj list so we need to make sure we dont run the dfs again on the same node which will cause a false call
        '''
        

        # first we will build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour == parent:
                    continue
                if not dfs(neighbour, node):
                    return False
            return True
        return dfs(0, - 1) and len(visited) == n
