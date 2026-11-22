class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        if not grid:
            return islands
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            grid[r][c] = "#"

            while queue:
                r, c = queue.popleft()

                for r_dir, c_dir in directions:
                    r_new, c_new = r + r_dir, c + c_dir

                    if (0 <= r_new < ROWS and
                        0 <= c_new < COLS and
                        grid[r_new][c_new] == "1"):
                        grid[r_new][c_new] = "#"
                        queue.append((r_new, c_new))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    bfs(row, col)
                    islands += 1
        return islands