class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = collections.defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        queue = collections.deque()
        queue.append(0)
        visited = [False] * n
        visited[0] = True

        while queue:
            node = queue.popleft()

            for neigh in graph[node]:
                if visited[neigh] == False:
                    visited[neigh] = True
                    queue.append(neigh)
        
        return all(visited)