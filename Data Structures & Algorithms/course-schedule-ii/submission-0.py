class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        """
        0 -> 1 -> 2
        1    1    1
        """
        for a, b in prerequisites:
            graph[a].append(b)

        UNVISTIED, VISITING, VISITED = 0, 1, 2
        states = [UNVISTIED] * numCourses
        res = []

        def dfs(i): # -> returns BOOLEAN, 
            if states[i] == VISITING:
                return False
            elif states[i] == VISITED:
                return True
            
            states[i] = VISITING

            for neigh in graph[i]:
                if not dfs(neigh):
                    return False
            
            res.append(i)
            states[i] = VISITED

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res