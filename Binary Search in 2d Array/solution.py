class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # since the flattened array is going to be sorted in ascending order
        # we need to find a way to index on the whole array in the cols and the rows
        # running binary search on len(matrix) * len(matrix[0])
        # using the mid calculated from that using the row = idx // cols and cols = idx % cols
        l ,r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False