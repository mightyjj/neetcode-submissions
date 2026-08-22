class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force: iterate through, find target, return true else return false
        # O(n^2)
        # optimize: check with last element of row
        # greater than last element of row, keep moving on
        # until find last element is greater
        # binary search on that row

        len_row = len(matrix[0]) - 1
        target_row = 0

        # prev_row = 1

        for prev_row in range(len(matrix)):
            # prev_row = 0
            if target > matrix[prev_row][len_row]:
                continue
            else:
                # do binary search
                lo, hi = 0, len_row

                while lo <= hi:
                    mid = lo + (hi - lo)
                    if matrix[prev_row][mid] == target:
                        return True
                    
                    if matrix[prev_row][mid] < target:
                        lo = mid + 1
                    else:
                        hi = mid - 1
        
        return False
            
        