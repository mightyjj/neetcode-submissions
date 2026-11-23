class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_queue = collections.deque()
        p_seen = set()

        a_queue = collections.deque()
        a_seen = set()

        ROWS, COLS = len(heights), len(heights[0])

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for j in range(COLS):
            p_queue.append((0, j))
            p_seen.add((0, j))
        
        for i in range(1, ROWS):
            p_queue.append((i, 0))
            p_seen.add((i, 0))
        
        for i in range(ROWS):
            a_queue.append((i, COLS - 1))
            a_seen.add((i, COLS - 1))
        
        for j in range(COLS - 1):
            a_queue.append((ROWS - 1, j))
            a_seen.add((ROWS - 1, j))

        def get_coords(queue, seen):
            while queue:
                i, j = queue.popleft()
                for i_dir, j_dir in directions:
                    i_new, j_new = i + i_dir, j + j_dir

                    if (0 <= i_new < ROWS and
                        0 <= j_new < COLS and
                        heights[i_new][j_new] >= heights[i][j] and
                        (i_new, j_new) not in seen):
                        queue.append((i_new, j_new))
                        seen.add((i_new, j_new))
            return seen

        p_coords = get_coords(p_queue, p_seen)
        a_coords = get_coords(a_queue, a_seen)

        return list(p_coords.intersection(a_coords))

                    


