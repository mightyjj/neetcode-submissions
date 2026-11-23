class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def capture(r, c):
            board[r][c] = "T"

            for r_dir, c_dir in directions:
                r_new, c_new = r + r_dir, c + c_dir
                if (0 <= r_new < ROWS and
                    0 <= c_new < COLS and
                    board[r_new][c_new] == "O"):
                    capture(r_new, c_new)


        # capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and 
                    (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    capture(r, c)

        # capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # uncapture unsurrounded regions(T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"