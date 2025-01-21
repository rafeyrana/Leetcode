class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        1. the simple solution would have been to keep a copy array and change that when we encounter a zer
        2. the other solution will be to keep single array for row and column to mark which columns and rows have to be zeroed out at the end
        3. the way to not use additional space is to bring that single row and column inside the array as the first row and column and use those as the markings
        '''
        rows = len(matrix)
        cols = len(matrix[0])
        row_zero = False
        for r in range(rows):
            for c in range(cols):
                # go through each element if 0 make the corresponding pointer row / col 0
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True
                        
        # now that we have marked them we will go through the first row and col and make the whole of them 0
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0