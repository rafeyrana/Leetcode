class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # so we can go to each index, if it is one and not in visited we increment the count by 1 of the islands and run a bfs on its neighbours from there until they all run into 0.
        # mark all the nodes in each value
        if not grid:
            return 
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            
            while q:
                cur_r, cur_c = q.popleft()
                # Check neighbors: up, down, left, right
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    n_r, n_c = cur_r + dr, cur_c + dc
                    # Ensure the neighbor is within bounds, not water, and unvisited
                    if (0 <= n_r < rows and 0 <= n_c < cols and
                        grid[n_r][n_c] == "1" and (n_r, n_c) not in visited):
                        q.append((n_r, n_c))
                        visited.add((n_r, n_c))
        
        # Traverse the grid
        for r in range(rows):
            for c in range(cols):
                # If it's land and not visited, it's a new island
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands