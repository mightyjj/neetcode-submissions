class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        """
        1) we build pacific/atlantic queue & seen
        2) helper func search(queue, seen)
            - bfs approach
            - it will check all directions (check within bounds)
            - then it will check that new cell if its >= curr_cell we add to seen and queue
            - returns seen (coords cells)
        3) we get coords of pacific/atlantic -> get the intersection
        """
        p_queue = collections.deque()
        p_seen = set()
        for i in range(COLS):
            p_queue.append((0, i))
            p_seen.add((0, i))
        
        for i in range(1, ROWS):
            p_queue.append((i, 0))
            p_seen.add((i, 0))

        a_queue = collections.deque()
        a_seen = set()
        for i in range(COLS):
            a_queue.append((ROWS - 1, i))
            a_seen.add((ROWS - 1, i))
        
        for i in range(ROWS - 1):
            a_queue.append((i, COLS - 1))
            a_seen.add((i, COLS - 1))
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def bfs(queue, seen):
            while queue:
                r, c = queue.popleft()

                for r_dir, c_dir in directions:
                    r_new, c_new = r + r_dir, c + c_dir

                    if (0 <= r_new < ROWS and
                        0 <= c_new < COLS and
                        heights[r_new][c_new] >= heights[r][c] and
                        (r_new, c_new) not in seen):
                        seen.add((r_new, c_new))
                        queue.append((r_new, c_new))

            return seen


        a_coords = bfs(a_queue, a_seen)
        p_coords = bfs(p_queue, p_seen)

        return list(a_coords.intersection(p_coords))


