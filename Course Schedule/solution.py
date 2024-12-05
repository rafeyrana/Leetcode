class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
       okay so in this case we will run a cycle detection algo on the graph, if there are no cycles we can take all the courses we need
       the thing to understand in this case is that we will use dfs from each src (course) to all its prerequisites and to keep a track of the nodes that we have already visited on this path. we will use a set called visitSet
       once we have vistited the node and all its neighbours we will go back up the call so we need to remove the current node from the visitSet for this path
       once we are going back up to the call we can add this fully explored node to the visited set and check on each time we visit a node if it has already been visited so we dont need to explore it all over again.

        '''
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre_req in prerequisites:
            preMap[crs].append(pre_req)
        visitSet = set() # contains all the nodes visited in this dfs path iteration // if we find the same node in this meaning there is a cycle
        already_visited = set() # contains all the nodes that have been fully visited with their neighbours
        def dfs(crs):
            if crs in already_visited:
                return True
            if crs in visitSet:
                # this is a cycle / loop
                return False
            if preMap[crs] == []: 
                # base case // has no prereqs can be taken directly
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            already_visited.add(crs)
            return True
        # loop over all the vertices to make sure we dont miss any in the case of disconnected graphs but we still have the vertices for them 
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True

            



