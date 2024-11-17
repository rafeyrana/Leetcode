class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # okay so we can explore all the paths in the grid of size word and add the ones which are equal to the word index, else we dont
        # to explore all the paths we will have to backtrack through all possible indexes as in at each cell we can check the up, down , right and left being valid and based on that we can iterate
        # the problem here is how to not go down the same path/ same cell, okay so we can return if we find a cell that is not the current index and then go to the next index
        # first lets code the basic solution up

        rows = len(board)
        cols = len(board[0])
        path = set()
        def backtracking(r, c, i):
            if i == len(word):
                return True
            if (r >= rows) or  (c >= cols) or (r < 0) or (c < 0) or ((r,c) in path) or (word[i] != board[r][c]):
                return False
            # only come here if one of the letters has been found
            path.add((r,c))
            result = backtracking(r, c + 1, i + 1) or backtracking(r + 1, c, i+ 1) or backtracking(r - 1, c, i + 1) or backtracking(r, c - 1, i + 1)
            path.remove((r,c))
            return result
        for r in range(rows):
            for c in range(cols):
                if backtracking(r, c, 0):
                    return True
        return False



        