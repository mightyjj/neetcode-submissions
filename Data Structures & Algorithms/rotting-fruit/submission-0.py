class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        visited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        time, fresh = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for r_dir, c_dir in directions:
                    r_new, c_new = r + r_dir, c + c_dir

                    if (0 <= r_new < ROWS and
                        0 <= c_new < COLS and
                        grid[r_new][c_new] == 1):
                        grid[r_new][c_new] = 2
                        queue.append((r_new, c_new))
                        fresh -= 1
            time += 1

        return time if not fresh else -1


