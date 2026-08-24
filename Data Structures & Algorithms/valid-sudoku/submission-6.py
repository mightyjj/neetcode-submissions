class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for row_i in range(len(board)):
            row = []
            for col_i in range(len(board[row_i])):
                value = board[row_i][col_i]
                if value != ".":
                    row.append(value)
            if len(row) != len(set(row)):
                return False
        # cols
        for col_i in range(len(board)):
            col = []
            for row_i in range(len(board[col_i])):
                value = board[row_i][col_i]
                if value != ".":
                    col.append(value)
            if len(col) != len(set(col)):
                return False
        
        # Squares
        for start_row_box in range(0, 9, 3):
            for start_col_box in range(0, 9, 3):
                box = []
                for row_i in range(start_row_box, start_row_box + 3):
                    for col_i in range(start_col_box, start_col_box + 3):
                        value = board[row_i][col_i]
                        if value != ".":
                            box.append(value)

                if len(box) != len(set(box)):
                    return False
        return True