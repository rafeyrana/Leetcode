from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows and columns
        for i in range(9):
            row_seen = set()
            col_seen = set()
            for j in range(9):
                # Check row
                if board[i][j] != ".":
                    if board[i][j] in row_seen:
                        return False
                    row_seen.add(board[i][j])

                # Check column
                if board[j][i] != ".":
                    if board[j][i] in col_seen:
                        return False
                    col_seen.add(board[j][i])

        # Check 3x3 subgrids
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                block_seen = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] != ".":
                            if board[i][j] in block_seen:
                                return False
                            block_seen.add(board[i][j])

        return True
