class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        using union find to find the number of connected components
        the union find algo contains:
        parent array
        rank array : size of the component / number of nodes in the component
        function to find the ultimate parent
        in union function for the two edges:

            1. get the ultimate parents of both // root parent
            2. get the rank for the ultimate parents
            3. combine them, join the parent with the smaller rank to the larger one
            4. Optimisation will be the path compression to assign the top level parent to the node to find to allow for faster search, when combining add the rank of the smaller component to the larger parent node

        to check if two nodes are part of the same component we will use a find function
            if both nodes have the same ultimate parent they are connected to the same component
        '''
        parent = [i for i in range(n)]
        rank = [1] * n # at the start each node on its own is a component of size 1

        def find(node):
            par = node
            while par != parent[par]:
                parent[par] = parent[parent[par]] # this is the path compression which will set the parents going up to the top most parent
                par = parent[par]
            return par
        

        def union(node1, node2):
            # 1. get the root parents of both nodes
            p1, p2 = find(node1), find(node2)

            # if no need to union because already in the same component
            if p1 == p2:
                return 0 # no union done

            # 2. Get ranks of the parents
            r1 , r2 = rank[p1], rank[p2]
        
            # #. Now we will compare the ranks and add the smaller component to the larger one, update parents and add ranks
            if r1 >= r2:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1 # we did a union
        
        components = n # initially we start off with each node as a seperate component, as we add them we will decrement the number of components
        for n1, n2 in edges:
            components -= union(n1, n2) # auto changes the components if combined
        return components