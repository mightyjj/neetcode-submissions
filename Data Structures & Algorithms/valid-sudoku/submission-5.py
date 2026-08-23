class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row_i in range(len(board)):
            row = []
            for col_i in range(len(board[row_i])):
                value = board[row_i][col_i]
                if value != ".":
                    row.append(value)
            if len(row) != len(set(row)):
                return False
        
        for col_i in range(len(board)):
            col = []
            for row_i in range(len(board[col_i])):
                value = board[row_i][col_i]
                if value != ".":
                    col.append(value)
            if len(col) != len(set(col)):
                return False

        for box_row_start in range(0, 9, 3):
            for box_col_start in range(0, 9, 3):
                box = []
                for box_row_i in range(box_row_start, box_row_start + 3):
                    for box_col_i in range(box_col_start, box_col_start + 3):
                        value = board[box_row_i][box_col_i]
                        if value != ".":
                            box.append(value)
                
                if len(box) != len(set(box)):
                    return False
        return True