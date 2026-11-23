class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        queue = collections.deque()
        visited = set()

        # find treasure chests
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        dist = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                grid[r][c] = dist

                for r_dir, c_dir in directions:
                    r_new, c_new = r + r_dir, c + c_dir

                    if (0 <= r_new < ROWS and
                        0 <= c_new < COLS and
                        (r_new, c_new) not in visited and
                        grid[r_new][c_new] == 2147483647):
                        queue.append((r_new, c_new))
                        visited.add((r_new, c_new))
                
            dist += 1