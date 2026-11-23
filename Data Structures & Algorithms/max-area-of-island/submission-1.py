class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
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

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area