class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
       # the best solution to this would be an inverse solution where we can store the max distance any fruit has from the rotten fruits of which there can be many
       # we can check this for all of them but since we need to also make sure all fruits are rotten in that time we need to keep a track of each node was visited or not
        # lets return a bool to indicate if we even found one

        rows = len(grid)
        cols = len(grid[0])
        max_dist = -1
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        def bfs(r,c):
            q = collections.deque()
            q.append((r, c))
            visited = set()
            visited.add((r,c))
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 2:
                        return steps, True
                   
                steps += 1
            return steps, False


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dist, found = bfs(r, c)
                    max_dist = max(max_dist, dist)

                    if not found :
                        return -1
        return 0 if max_dist == -1 else max_dist
                    
        

        