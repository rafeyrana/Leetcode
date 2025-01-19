class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        using the union find algorithm with rank to find cycle creating edges, we will be connecting the nodes together if they are not previously connected, if they are then we can just return that one.
        the way to check for connection is to the use find function and check if they have the same top level parent
        iterate through all the edges, check if the union find can insert the edge or not, if they have the same parent, it is adding a cycle in this code meaning we can remove that edge
        '''
        n = len(edges) # we have been told we have n edges now
        parent = [i for i in range(n + 1)] # nodes are 1 indexed not starting from 0
        rank = [1] * (n + 1)
        

        def find(node): # get the top level parent for each
            par = node
            while par != parent[par]:
                parent[par] = parent[parent[par]] # optimisation for path compression
                par = parent[par]
            return par


        def union(n1, n2): # add nodes to the components
            # 1. get top level parents
            p1 , p2 = find(n1),find(n2)
            # if they are the same then it is already connected and hence this edge is adding a cycle
            if p1 == p2:
                return False
            # if not a cycle we will continue to add them
            # 2. get rank of the parents
            r1, r2 = rank[p1], rank[p2]
            # add the smaller rank component to the one with the larger rank and update the rank
            if r1 >= r2:
                parent[p2] = p1
                rank[p1] += r2
            else:
                parent[p1] = p2
                rank[p2] += r1
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        