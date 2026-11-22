class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = collections.deque()

        def addRoom(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r, c) in visited or grid[r][c] == -1):
                return
            visited.add((r, c))
            queue.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        
        dist = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            
            dist += 1