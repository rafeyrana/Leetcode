class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # same as number of islands but this time we can keep a track of the area in the bfs function and use max on it on each iteration.

        if not grid :
            return 0
        rows , cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            area = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_r , new_c = row + dr , col + dc
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] != 0 and (new_r, new_c) not in visited:
                        q.append((new_r , new_c))
                        visited.add((new_r , new_c))
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and (r, c) not in visited:
                    island_area = bfs(r, c)
                    max_area = max(island_area, max_area)

            
        return max_area