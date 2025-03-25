class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # since we need to optimally check if different regions (rows, cols , subbox) contain the numbers without duplication
        # in the least time we need to use sets for this problem, we will only add to this set and check the sets if the current position is not a "."
        # now to check for each region we will need one set
        # 9 rows = 9 sets
        # 9 cols = 9 cols
        # 9 subbox = 9 subboxes
        # the indexing for the rows and cols is simple using a double loop but how do we figure out which subbox its in
        # maybe we can use some indexing combining the rows and cols
        '''
        lets try some examples
        2,2 = (2 // 3) * 3 + 2 // 3 = 0 + 0 = 0
        7,8 = (7 // 3) * 3 + 8 // 3 = 9
        6,3 = (6 // 3) * 3 + 3 // 3 = 8
        4,8 = = 6
        1,8 = = 3
        '''
        rows, cols , subboxes = [set() for _ in range(len(board))], [set() for _ in range(len(board[0]))], [set() for _ in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[0])):
                pos = board[r][c]
                if pos != ".":
                    # only check for the conditions if the current index position is not empty
                    if pos in rows[r]:
                        return False
                    if pos in cols[c]:
                        return False
                    if pos in subboxes[(r // 3) * 3 + (c // 3)]:
                        return False
                    rows[r].add(pos)
                    cols[c].add(pos)
                    subboxes[(r // 3) * 3 + (c // 3)].add(pos)
        return True
