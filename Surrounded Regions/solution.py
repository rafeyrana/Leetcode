class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        okay so in this case we just need to check which of the Os are on the border and which ones arent
        reverse thinking in this case would be lets find all the os we can access via the borders and then explore those to find more connected / unsurrounded Os if we dont find any then we can move on because we gucci
        in the end we can come back to the board after marking the reachable Os with T and then convert the remaining surrounded Os to Xs and the marked Os back to Os
        '''

        ROWS = len(board)
        COLS = len(board[0])
        def bfs():
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            q = collections.deque()
            for r in range(ROWS):
                for c in range(COLS):
                    # only add the Os on the border
                    if (r == 0 or r ==  ROWS -1) or (c == 0 or c == COLS - 1) and board[r][c] == "O":
                        q.append((r,c))
            while q:
                row, col = q.popleft()
                if board[row][col] == "O":
                    board[row][col] = "T"
                    for dx, dy in directions:
                        new_row , new_col = row + dx, col + dy
                        if (0 <= new_row < ROWS) and (0 <= new_col < COLS):
                            q.append((new_row, new_col))

        bfs()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
                    
       


        