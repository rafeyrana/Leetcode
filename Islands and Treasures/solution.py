class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # this can be done using dfs with counting depth and using the minimum one from each neighbour one
        # or if we dont wanna go through the whole thing we can just traverse it usign bfs using the levels as the distance

        # depending on the graph being sparse or highly connected or deep or not we can choose either strategy

        # assuming the graph is dense but not deep we can use bfs
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647
        def bfs(r, c):
            q = collections.deque([(r, c)])
            visited = set([(r, c)])
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    # if this is not it lets check on the right left etc
                    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dx, dy in directions:
                        new_row = row + dx
                        new_col = col + dy
                        if new_row in range(rows) and new_col in range(cols) and (new_row, new_col) not in visited and grid[new_row][new_col] != -1:
                            visited.add((new_row, new_col))
                            q.append((new_row, new_col))
                steps += 1
            return INF


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
         





        