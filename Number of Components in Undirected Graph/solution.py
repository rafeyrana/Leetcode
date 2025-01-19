class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
            
        adj = [[] for _ in range(n)]
        components = 0
        # make the adjacency list and start exploring
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        # now that we have made the adjacency list for the lists we will now use the same approach as the number of islands here, lets do a dfs search on this and keep adding the nodes that we see in the visited to it
        visited = [False for _ in range(n)]
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for nei in adj[node]:
                dfs(nei)
            
        for node in range(n):
            if not visited[node]:
                dfs(node)
                components += 1
        return components
        
        