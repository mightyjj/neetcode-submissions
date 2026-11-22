class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            grid[r][c] = 2
            res = 1

            while queue:
                r, c = queue.popleft()
                
                for r_dir, c_dir in directions:
                    r_new, c_new = r + r_dir, c + c_dir

                    if (0 <= r_new < ROWS and
                        0 <= c_new < COLS and
                        grid[r_new][c_new] == 1):
                        grid[r_new][c_new] = 2
                        queue.append((r_new, c_new))
                        res += 1
            return res

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    max_area = max(max_area, bfs(row, col))
        
        return max_area