class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)

        UNVISTIED, VISITING, VISITED = 0, 1, 2
        states = [UNVISTIED] * numCourses

        def dfs(i):
            if states[i] == VISITING:
                return False
            elif states[i] == VISITED:
                return True
            
            states[i] = VISITING

            for neigh in graph[i]:
                if not dfs(neigh):
                    return False
            
            states[i] = VISITED

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True