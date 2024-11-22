class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
      
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
                    for dx, dy in directions:
                        new_row = row + dx
                        new_col = col + dy
                        if ( 0 <= new_row < rows) and (0 <= new_col < cols) and (new_row, new_col) not in visited and grid[new_row][new_col] != 0:
                            q.append((new_row, new_col))
                            visited.add((new_row, new_col))
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
                    
        

        