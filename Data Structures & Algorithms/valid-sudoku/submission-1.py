class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(list)
        rows = collections.defaultdict(list)
        squares = collections.defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[r])):
                value = board[r][c]
                if value == ".":
                    continue
                    
                if (value in cols[c]) or \
                    (value in rows[r]) or \
                    (value in squares[(r // 3, c //3)]):
                    return False

                cols[c].append(value)
                rows[r].append(value)
                squares[(r // 3, c // 3)].append(value)

        return True