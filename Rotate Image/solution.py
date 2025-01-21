class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # the rotate by 90 transformation can be split down into two different transformations: flip by 180 and then take transpose

        # flip 180
        matrix.reverse()

        # transpose
        rows = len(matrix[0])
        cols = len(matrix)
        for r in range(rows):
            for c in range(r + 1, cols): # only visit the top triangle not the bottom one
                matrix[r][c] , matrix[c][r] = matrix[c][r], matrix[r][c]