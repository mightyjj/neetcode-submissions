class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows * cols - 1

        while l <= r:
            m = (l + r) // 2

            row = m // cols
            col = m % cols

            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                l = m + 1
            else:
                r = m - 1
        
        return False