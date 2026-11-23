class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

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


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands