class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # the solution for this isnt a clever algorithm but a neat observation. the 90 degree clockwise rotation transformation can be broken into transpose + row reversal
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):  # Swap only the upper triangle to avoid redundant swaps
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # once we have the transpose we just have to reverse the rows in place
        for row in matrix:
            row.reverse()

    
        