class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        the rule for the queens not being able to attack each other is that they cannot be in the same row, col or diagnol as any other queen
        its simple to check for row or col but the way to check for the diagnols is a trick
        on the positive diags (bottom to up), the sum of the r + c will remain the same for example on the middle pos diag for n = 3 (3 + 0 = 3, 2 + 1 = 3 , 1 + 2 = 3 , 0 + 3 = 3)
        a similar relationship exists on the difference or r and c (r - c) on the neg diagonal
        
        we have to explore all solutions so we will take a backtracking approach and instead of checking for each and every r , c combo since we know we can only have them in one row or col each we can go row by row
        we will hashsets to keep a track of the col, posDiag and negDiag.
        '''
        col = set()
        posDiag = set()
        negDiag = set()
        results = []
        board = [["."] * n for _ in range(n)]

        def backtracking(r):
            if r == n: # meaning we have explored all rows for this combination of queens
                board_copy = ["".join(row) for row in board]
                results.append(board_copy)
                return
            
            # now for each row we will check all columns and try to place a queen there, if we can place a queen there we will place it there and move the row forward to keep checking further rows to place the queens
            for c in range(n):
                # if there is a queen in the same column, or same diagnols pos and neg we will move on the next col
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                # meaning we can place a queen here
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                # now that we have added the queen here we can try to find where to place the queen on the next row
                backtracking(r + 1)
                # once done exploring
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        backtracking(0)
        return results

